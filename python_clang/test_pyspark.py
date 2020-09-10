from pyspark import SparkConf
from pyspark.sql import SparkSession
import traceback
 
appname = "test"#任务名称
master ="local"#单机模式设置
'''
local: 所有计算都运行在一个线程当中，没有任何并行计算，通常我们在本机执行一些测试代码，或者练手，就用这种模式。
local[K]: 指定使用几个线程来运行计算，比如local[4]就是运行4个worker线程。通常我们的cpu有几个core，就指定几个线程，最大化利用cpu的计算能力
local[*]: 这种模式直接帮你按照cpu最多cores来设置线程数了。
'''
try:
    conf = SparkConf().setAppName(appname).setMaster(master)#spark资源配置
    spark=SparkSession.builder.config(conf=conf).getOrCreate()
    sc=spark.sparkContext
    words = sc.parallelize(
        ["scala",
         "java",
         "hadoop",
         "spark",
         "akka",
         "spark vs hadoop",
         "pyspark",
         "pyspark and spark"
         ])
    counts = words.count()
    print("Number of elements in RDD is %i" % counts)
    sc.stop()
    print('计算成功！')
except:
    sc.stop()
    traceback.print_exc()#返回出错信息
    print('连接出错！')

"""
>>>

SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/home/gupengxiang/.local/lib/python3.6/site-packages/pyspark/jars/slf4j-log4j12-1.7.16.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/opt/cloudera/parcels/CDH-5.11.0-1.cdh5.11.0.p0.34/jars/slf4j-log4j12-1.7.5.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Number of elements in RDD is 8
计算成功！
"""



from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf()
conf.setMaster('yarn')
conf.setAppName('spark-yarn')
conf.setExecutorEnv('HADOOP_CONF_DIR','$HADOOP_HOME/etc/hadoop')
conf.setExecutorEnv('YARN_CONF_DIR','$HADOOP_HOME/etc/hadoop')
sc = SparkContext(conf=conf)


def mod(x):
    import numpy as np
        return (x, np.mod(x, 2))
    rdd = sc.parallelize(range(1000)).map(mod).take(10)
    print(rdd)

"""
>>>
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/home/gupengxiang/.local/lib/python3.6/site-packages/pyspark/jars/slf4j-log4j12-1.7.16.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/opt/cloudera/parcels/CDH-5.11.0-1.cdh5.11.0.p0.34/jars/slf4j-log4j12-1.7.5.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
20/06/16 18:06:22 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
20/06/16 18:06:22 WARN yarn.Client: Neither spark.yarn.jars nor spark.yarn.archive is set, falling back to uploading libraries under SPARK_HOME.

[(0, 0), (1, 1), (2, 0), (3, 1), (4, 0), (5, 1), (6, 0), (7, 1), (8, 0), (9, 1)]
"""
