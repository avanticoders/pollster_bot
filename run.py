from pollster.pollbot import Pollbot

with Pollbot(teardown=True) as bot:
    bot.main_page()
    bot.click_view_link()
    bot.gender_vote(gender="female")
    bot.many_genders_vote(["male", "female", "male", "female"])
    # bot.adult_child_vote(vote_value="adult")
    # bot.many_adult_child_vote(["adult", "child", "child", "adult"])
