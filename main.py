import json
import urllib.request
import pprint
import random


def sgn(x):
    return ['', '+'][int(x) > 0]


def gildedText(postData):
    if int(postData['gilded']) > 0:
        return ', %s gilded' % postData['gilded']
    else:
        return ''


def getParsedJson(url):
    try:
        shittyJson = urllib.request.urlopen(url).read().decode('utf-8')
    except Exception as e:
        print("Could not connect to reddit, sorry mate, it's awful.")
        print("Error: %s" % e)
        exit(0)

    try:
        parsedJson = json.loads(shittyJson)
    except Exception as e:
        print("Sorry mate, could not figure out how to parse that json stuff.")
        print("Error: %s" % e)
        exit(0)

    return parsedJson


def chooseSomePost(parsedJson):
    try:
        posts = parsedJson['data']['children']
    except Exception as e:
        print("Apparently, your parsed json has no children.")
        print("Error: %s" % e)
        exit(0)

    try:
        chosenPost = random.choice(posts)
    except Exception as e:
        print("Apparently, there are no posts to choose from.")
        print("Error: %s" % e)
        exit(0)

    return chosenPost


def formatOutput(chosenPost):
    try:
        chosenPostData = chosenPost['data']

        out = "(score: %s%s%s)\n> %s\n\n> %s" % (
                sgn(chosenPostData['score']),
                chosenPostData['score'],
                gildedText(chosenPostData),
                chosenPostData['title'],
                chosenPostData['selftext']
                )

    except Exception as e:
        print("Something went wrong while formatting the output.")
        print(e)
        exit(0)

    return out


def main():
    subreddit = 'MeanJokes'
    criteria = 'hot'
    url = 'https://www.reddit.com/r/%s/%s.json' % (subreddit, criteria)

    parsedJson = getParsedJson(url)
    chosenPost = chooseSomePost(parsedJson)
    output = formatOutput(chosenPost)

    print(output)


if __name__ == '__main__':
    main()
