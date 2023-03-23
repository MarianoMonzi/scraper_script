import requests
import lxml.html as html

HOME_URL = 'https://www.lastepochtools.com/builds/'

XPATH_CLASS_BUILDS = '//a/div[@class="title"]/text()'
XPATH_SKILLS_BUILDS = '//div[@class="row skills"]/div/a[@class="link"]/text()'
XPATH_VERSION = '//div[@class="inner"]/text()'
XPATH_LINK_VIDEO = '//div[@class="guide"]/a/@href'

list_skills = []
list_class_builds = []
list_version = []
list_videos = []
tamaño_sublista = 5


def parse_builds():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            class_builds = parsed.xpath(XPATH_CLASS_BUILDS)

            for build in class_builds:
                list_class_builds.append(build)

            parse_skills()
            parse_version()
            parse_link_video()

    except ValueError as ve:
        print(f'Error: {ve}')


def parse_skills():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            skills = parsed.xpath(XPATH_SKILLS_BUILDS)

            for i in range(0, len(skills), tamaño_sublista):
                sublista = skills[i:i+tamaño_sublista]
                list_skills.append(sublista)

    except ValueError as ve:
        print(f'Error: {ve}')


def parse_version():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            versions = parsed.xpath(XPATH_VERSION)

            for version in versions:
                list_version.append(version)

    except ValueError as ve:
        print(f'Error: {ve}')


def parse_link_video():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            videos = parsed.xpath(XPATH_LINK_VIDEO)

            for video in videos:
                list_videos.append(video)

    except ValueError as ve:
        print(f'Error: {ve}')

def parse_build_final():
    builds = []
    for mastery, skill, version, video in zip(list_class_builds, list_skills, list_version, list_videos):
        build = {'Mastery': mastery, 'Skills': skill, 'Version': version, 'Video': video}
        builds.append(build)
    
    print(builds)


def run():
    parse_builds()
    parse_build_final()
    


if __name__ == '__main__':
    run()
