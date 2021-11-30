import json
import time
from datetime import datetime

from project.Connectors.DB.PostgresConnector import PostgresConnector
from project.DB.Getters.YouTube.ChannelInfoGetter import ChannelInfoGetter
from project.Reporters.ReportSenders.MailSender import MailSender


class VideosCountReporter:
    def __init__(self):
        self.channel_info_getter = ChannelInfoGetter(PostgresConnector())
        self.mail_sender = MailSender()

    def send_report(self):
        while True:
            sending_ts = datetime.now()
            subject = "Report for %s" % sending_ts.strftime('%Y-%m-%d %H:%M')

            json_to_send = {}
            for line in self.channel_info_getter.get_videos_count():
                json_to_send[line[0]] = {"videosCount": line[1]}

            file_data = json.dumps(json_to_send, indent=4, sort_keys=True, ensure_ascii=False)
            self.mail_sender.send(file_data, "report.json", subject)
            time.sleep(3600)


