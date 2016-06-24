from share.normalize import *  # noqa


class Person(Parser):
    given_name = ParseName(ctx.author_name).first
    family_name = ParseName(ctx.author_name).last


class Contributor(Parser):
    person = ctx


class Manuscript(Parser):
    title = ctx.title
    description = ctx.description
    contributors = ctx.authors['*']
    # publish_date = ParseDate(ctx.published_date)

# Extra Field
# Voting System
