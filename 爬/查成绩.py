import re
import requests
import pandas as pd

baseURL = "https://ljcj.hfzsks.org/"
postURL = "https://ljcj.hfzsks.org/list_score/cj_out.php"
cookieName = "PHPSESSID"
subject2re = {}
subjectList = ["语文", "数学", "英语", "道德与法治", "历史", "物理", "化学", "体育", "实验", "政策加分", "总分"]

def getCookie(url):
    response = requests.get(url)
    cookieValue = response.cookies.get(cookieName)
    return {cookieName: cookieValue}


def getHtml(fzkh: str, name: str, cookie):
    data = {
        "find_fzkh": fzkh,
        "find_fxm": name,
        "seach_name": "查  询"
    }
    response = requests.post(postURL, data=data, cookies=cookie)
    return response.content.decode()

def getSubjectScores(content: str):
    subject2score = {}
    for key, value in subject2re.items():
        subject2score[key] = value.findall(content)[0]
    return subject2score

def initSubjectRE():
    for subject in subjectList:
        subject2re[subject] = re.compile('''bgcolor='#CCCCCC'>''' + subject + '''</td>\s*<td align="center" width="120">(.*?)</td>''')
    return subject2re

if __name__ == '__main__':
    data = pd.read_excel("./中考.xlsx")
    cookie = getCookie(baseURL)
    initSubjectRE()
    scoreList = {subject : [] for subject in subjectList}
    print("--------开始爬取--------")
    for index, row in data.iterrows():
        print("已爬取： 姓名：" + row['姓名'] + "; 准考证：" + str(row['中考准考证号']) + "\n")
        html = getHtml(row['中考准考证号'], row['姓名'], cookie)
        scores = getSubjectScores(html)
        for key, value in scores.items():
            scoreList[key].append(value)
    for key, value in scoreList.items():
        data[key] = value
    print("--------排序--------")
    data = data.sort_values(by="总分", ascending=False)
    print("--------导出数据到excel--------")
    with pd.ExcelWriter('test.xlsx') as writer:
        data.to_excel(writer, sheet_name='data')
