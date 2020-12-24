import json
from pyspark.sql import SparkSession

spark = SparkSession\
        .builder\
        .appName("wordcount")\
        .getOrCreate()

sc = spark.sparkContext
txt = sc.textFile("hdfs:///user/gupengxiang/hello.txt")
#txt = sc.textFile("hdfs:///user/lichen/hb2-vpc-92/info.log.20191110")

textfileRDD = txt
#wordsRDD = textfileRDD.flatMap(lambda line: line.split(" "))
#pairsRDD =  wordsRDD.map(lambda word: (word, 1))
#frequenciesRDD = pairsRDD.reduceByKey(lambda a, b: a + b)

print("\n\n")
print(textfileRDD.first())
#print("\n\n")
#print(textfileRDD.collect())
#print("\n\n")
#print(wordsRDD.collect())
#print("\n\n")
#print(pairsRDD.collect())
#print("\n\n")
#print(frequenciesRDD.collect())


def make_parallel_line(line: str) -> list:
    """
    格式化日志
    """
    data = line.split("###")[-1]
    try:
        data = json.loads(data)
    except Exception:
        data = {}
    line = [data.get("auth_code"), data.get("channel"), data.get("device_id"), data.get("event_name")]
    return line

def event_ruler(fmt_line: list) -> bool:
    """
    事件类型判断规则器
    """
    sign = False
    if fmt_line[-1] == "/dm_api/check_followup":
        sign = True
    return sign

##########################  go  #############

num_fiterJ = textfileRDD.map(make_parallel_line)
#filter_check_followup = num_fiterJ.count()
filter_check_followup = num_fiterJ.collect()
filter_check_followup_num = num_fiterJ.filter(event_ruler).count()
#num_fiterJ = textfileRDD.filter(lambda s: '###' in s).count()
print("\n\n")
print("\n\n")
print(f"num_fiterJ: {num_fiterJ} \n")
print(f"filter_check_followup: {filter_check_followup} \n")
print(f"filter_check_followup_num: {filter_check_followup_num} \n")


# done!
spark.stop()


"""
输出:
    print(textfileRDD.first())
    >>> logstash###octopus_dev###action###{"controller":"service","fields.msg":null,"level":"info","msg":"ServiceController.ListServerStatus","request_id":"1198632365094604800","time":"2019-11-25T00:00:00+08:00","time_cost":17.429262}


    print(f"num_fiterJ: {num_fiterJ} \n")
    >>> num_fiterJ: PythonRDD[5] at RDD at PythonRDD.scala:53

    print(f"filter_check_followup: {filter_check_followup} \n")
    >>> filter_check_followup: [[None, None, None, None], ['', '', '', '/dm_api/check_followup'], [None, None, None, None], ['', '', '', '/dm_api/check_followup'], [None, None, None, None], ['', '', '', '/dm_api/check_followup'], [None, None, None, None], ['', '', '', '/dm_api/check_followup'], [None, None, None, None], ['', '', '', '/dm_api/check_followup'], [None, None, None, None], ['', '', '', '/dm_api/check_followup'], [None, None, None, None], ['', '', '', '/dm_api/check_followup'], [None, None, None, None], ['', '', '', '/dm_api/check_followup'], [None, None, None, None], ['', '', '', '/dm_api/check_followup'], [None, None, None, None], ['', '', '', '/dm_api/check_followup']]

    print(f"filter_check_followup_num: {filter_check_followup_num} \n")
    >>> filter_check_followup_num: 10

"""
