from project.Reporters.YouTubeReporters.VideosCountReporter import VideosCountReporter


def main():
    video_reporter = VideosCountReporter()
    video_reporter.send_report()


if __name__ == '__main__':
    main()
