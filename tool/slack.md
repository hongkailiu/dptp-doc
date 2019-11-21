# Slack

https://coreos.slack.com/messages/

## threads

https://slackhq.com/threaded-messaging-comes-to-slack

## reactions

https://slackhq.com/722-ways-to-say-i-got-your-message

## reminders

https://get.slack.help/hc/en-us/articles/208423427-Set-a-reminder#desktop-1

```
###Talk to slackbot, then the message will show up in the target person/channel
###Add new reminders
/remind #aos-svt-qe “svt-scrum starts at 9:45 https://bluejeans.com/540285617” at 9:40AM every weekday
/remind #aos-svt-qe "aos-qe-us sprint-retro starts at 21:15 https://bluejeans.com/540285617?src=calendarLink" on October 23, at 21:10PM,every 3 weeks
/remind #aos-svt-qe “@here scrum meeting with Xiaoli starts at 8:15PM” at 8:10PM
###list reminders
/remind list

/remind me "@hongkliu is build-cop on duty today" on September 20, at 8:00AM
/remind #team-dp-testplatform "@hongkliu holds ops duty on Monday, Nov 18" on November 18 2019, at 09:00AM
```

Note that whether or not you get notifications of those reminders depends on your notification setting on the channel. We could also monify it in the way with @channel (see [here](https://get.slack.help/hc/en-us/articles/202009646-Notify-a-channel-or-workspace) for details).

## Google calendar integration

It works but I need to figure out how to prevent others abusing the settings.
The advantage (vs reminder) of this integration is to sync automatically with Google calenders.

## Github integration

https://github.com/integrations/slack

```
/github subscribe https://github.com/openshift/svt
```
