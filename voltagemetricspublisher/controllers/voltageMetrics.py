from cement import Controller, ex
from cement.utils.version import get_version_banner
from ..core.version import get_version
import threading
from services.extractionService import ExtractionService
from services.kafkaService import KafkaService

VERSION_BANNER = """
Console Application to publish Voltage Metrics to Kafka. %s
%s
""" % (get_version(), get_version_banner())

class VoltageMetrics(Controller):
    class Meta:
        label = 'Voltage Metrics'

        # text displayed at the top of --help output
        #description = 'Console Application to publish Voltage Metrics to Kafka.'

        # text displayed at the bottom of --help output
        #epilog = 'Usage: voltagemetricspublisher command1 --foo bar'

        # controller level arguments. ex: 'voltagemetricspublisher --version'
        # arguments = [
        #     # add a version banner
        #     (['-v', '--version'],
        #      {'action': 'version',
        #         'version': VERSION_BANNER}),
        # ]

    def __init__(self):
        self.kafkaService = KafkaService()
        self.extractionService = ExtractionService()

    @ex(
        help='example sub command1',

        # sub-command level arguments. ex: 'voltagemetricspublisher command1 --foo bar'
        arguments=[
            # add a sample foo option under subcommand namespace
            (['-f', '--foo'],
             {'help': 'notorious foo option',
                'action': 'store',
                'dest': 'foo'}),
        ],
    )
    def start(self):
        """Starting Voltage Metrics Publish."""
        threading.Timer(1.0, self.start).start()

        extractedMetrics = self.extractionService.getGpioValues()
        self.kafkaService.publishToTopic(self.app.config.get("kafka_settings", "topic_name"), extractedMetrics)