from mega import Mega
from download import Download
from authorMapper import AuthorMapper

def main():
    MEGA_ACCOUNT = ""
    MEGA_PASSWORD = "."

    SEARCH_NAME = ""

    DOWNLOAD_ID = 0
    DOWNLOAD_NAME = ""
    DOWNLOAD_COUNT = 1

    if SEARCH_NAME != "":
        authorMapper = AuthorMapper()
        rows = authorMapper.search_author(SEARCH_NAME)
        # total = len(rows)
        print(f"共找到 {len(rows)} 条结果:")
        for row in rows:
            print(dict(row))
        raise SystemExit()


    mega = Mega()
    mega.login_if_needed(MEGA_ACCOUNT, MEGA_PASSWORD)

    download = Download()
    download.start(DOWNLOAD_ID, DOWNLOAD_NAME, DOWNLOAD_COUNT)


if __name__ == "__main__":
    main()