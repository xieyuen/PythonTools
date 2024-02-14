import requests
from jsonpath import jsonpath


class Constants:
    musicNotFoundMsg = "对不起，暂无搜索结果!"
    searchURL = 'https://music.liuzhijin.cn/'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        # 判断请求是异步还是同步
        "x-requested-with": "XMLHttpRequest",
    }
    platformInfo = (
        "脚本支持以下平台:\n"
        "1.网易云:netease\n"
        "2.QQ:qq\n"
        "3.酷狗:kugou\n"
        "4.酷我:kuwo\n"
        "5.百度:baidu\n"
        "6.喜马拉雅:ximalaya\n"
        "请选择平台: "
    )
    platformMap = {
        k: v for keys, v in
        (
            (
                (
                    '1', 'n', 'net', 'wy', 'wyy', 'wangyi', 'wangyiyun', 'netease', '网易', '网易云', '网易云音乐'
                ), 'netease'
            ), (
                (
                    '2', 'q', 'qq', 'qqmusic', 'qqyinyue', 'qq音乐', 'qq 音乐'
                ), 'qq'
            ), (
                (
                    '3', 'kg', 'ku', 'kou', 'gou', 'kugou', '酷狗'
                ), 'kugou'
            ), (
                (
                    '4', 'kw', 'ko', 'wo', 'kuwo', '酷我'
                ), 'kuwo'
            ), (
                (
                    '5', 'b', 'bd', 'bu', 'baidu', '百度'
                ), 'baidu'
            ), (
                (
                    '6', 'x', 'xi', 'xmly', 'xmla', 'ximalaya', '喜马拉雅'
                ), 'xiamlaya'
            ),
        )
        for k in keys
    }


class Crawler:
    @staticmethod
    def getParam(name: str, platform: str) -> dict:
        return {
            "input": name,
            "filter": "name",
            "type": Constants.platformMap[platform],
            "page": 1,
        }

    @staticmethod
    def getMusicContentData(url: str) -> bytes:
        return requests.get(url).content

    def download(self, url, author, title, path="./"):
        print(f'{author}-{title} 正在下载...')
        with open(f"{path}/{author}-{title}.mp3", mode='wb') as f:
            f.write(self.getMusicContentData(url))

    def main(self):
        param = self.getParam(
            name=input("请输入歌曲名:"),
            platform=input(Constants.platformInfo)
        )
        json_text = requests.post(
            url=Constants.searchURL,
            data=param,
            headers=Constants.headers,
        ).json()

        titles = jsonpath(json_text, '$..title')
        authors = jsonpath(json_text, '$..author')
        urls = jsonpath(json_text, '$..url')

        if not titles:
            raise ValueError(Constants.musicNotFoundMsg)

        print("-------------------------------------------------------\n查找到以下歌曲:\n")
        for index, (t, a) in enumerate(zip(titles, authors)):
            print(f"{index + 1} | {t} - {a}")

        indexes = input("请输入您想下载的歌曲版本(填序号,多个用英文逗号隔开):").split(',')
        savePath = input("请输入保存路径(空则为脚本所在路径):")
        for i in indexes:
            i = int(i) - 1
            self.download(urls[i], authors[i], titles[i], savePath)


if __name__ == '__main__':
    Crawler().main()
