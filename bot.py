from instapy import InstaPy

#login
session = InstaPy(username ="put your username", password="put your password")
session.login()

#like
session.like_by_tags(['javscript', 'python'], amount=5)

#follow
session.set_do_follow(True, percentage=25)

#comment
session.set_do_comment(True, percentage=50)
session.set_comments(['Like it..','Nice post', u'Nice post 😇' ])

session.end()