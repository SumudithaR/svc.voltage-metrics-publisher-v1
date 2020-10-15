
from cement import App
from pykafka import KafkaClient, Topic
from cement.utils.version import get_version_banner

class KafkaService(App):
    def __init__(self):  
        kafkaHost = self.config.get("kafka_settings", "host")
        self.kafkaClient = KafkaClient(hosts=kafkaHost)
        
        if self.kafkaClient is None:
            print("Failed to instantiate Kafka Client.")

    def publishToTopic(self, topicName, item):
        if topicName is None:
            print('Provided Topic Name is invalid. TopicName: %s' % topicName)

        if item is None:
            print('Provided Data item is invalid.')

        rawVoltageMetricsTopic = self.kafkaClient.topics['raw-voltage-metrics']
        
        if rawVoltageMetricsTopic is None:
            self.kafkaClient.topics._create_topic('raw-voltage-metrics')
            rawVoltageMetricsTopic = self.kafkaClient.topics['raw-voltage-metrics']
        
        with rawVoltageMetricsTopic.get_sync_producer() as producer:
            producer.produce(item)