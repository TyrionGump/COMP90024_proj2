# ====================================
# COMP90024 Cluster and Cloud Computing
# Group 22 - Assignment 2
# Ran Liang 1162222
# Yulun Huang 910398
# Yubo Sun 1048638
# Yanhao Wang 1142087
# Xindi Fang 749394
# Last Updated: 2021-05-25
# Description:Create all related views used by the front-end. Included all information for the scenario: vaccine, time, unemployment, source.
# Related DB Name: no-duplicate-twitter
# MapReduce Program Language: JavaScript
# Comment: This file would take a long period of time updating the database. Be aware while Execution.
# =========================

import logging
import couchdb

couchclient = couchdb.Server('http://admin:admin@172.26.130.240:5984/')
db = couchclient['no_duplicate_twitter']

if db.__contains__('_design/climate_analysis'):
    db.__delitem__('_design/climate_analysis')
if db.__contains__('_design/vaccine_analysis'):
    db.__delitem__('_design/vaccine_analysis')
if db.__contains__('_design/unemployment_analysis'):
    db.__delitem__('_design/unemployment_analysis')
if db.__contains__('_design/time_analysis'):
    db.__delitem__('_design/time_analysis')
if db.__contains__('_design/source_analysis'):
    db.__delitem__('_design/source_analysis')



def createView(dbConn, designDoc, viewName, mapFunction, reduceFunction):
    data = {
        "_id": f"_design/{designDoc}",
        "views": {
            viewName: {
                "map": mapFunction,
                "reduce": reduceFunction
            }
        },
        "language": "javascript",
        "options": {"partitioned": False}
    }
    logging.info(f"creating view {designDoc}/{viewName}")
    dbConn.save(data)


def addView(db, designDoc, viewName, mapFunction, reduceFunction):
    db_add = db['_design/' + designDoc]['views'].keys()
    keys = []
    mapF = []
    for i in db_add:
        print(i)
        keys.append(i)
        func = db['_design/' + designDoc]['views'].get(i)
        mapF.append(func)
    db.__delitem__('_design/' + designDoc)
    new_views = {}
    for j in range(keys.__len__()):
        new_views[keys[j]] = mapF[j]
    new_views[viewName] = {"map": mapFunction, "reduce": reduceFunction}
    data = {
        "_id": f"_design/{designDoc}",
        "views": new_views,
        "language": "javascript",
        "options": {"partitioned": False}
    }
    db.save(data)


map_function_weather = """function (doc) {
  const split = doc.text;
  const weather = ["weather","rain","cloud","rainbow","temperature","shower","sunrise","dry","tornado","sunset","humidity","cold",
          "heat","wind","cloudy","heat wave","fog","breeze","humid","lightning","blustery","humidity","thunder","snow",
          "heat index","thunderstorm","downpour","drought","temperate","moisture","drizzle","warm","hail","icicle","climate",
          "storm","flood","muggy","gale","flash flood","atmosphere","sky"];

var word_find = [];
var counter = [];

var arr = split.toLowerCase().split(/[.,\/ -!?'"#@]/);
var i, j;
var total = 0
for (i = 0; i < arr.length; i++) {
  for (j = 0; j < weather.length; j++) {
    if (arr[i] == weather[j]) {
      var word = arr[i];
      if (word_find.includes(word) == false) {
        word_find.push(word);
        counter.push(doc.polarity);
      } else {
        var index = word_find.indexOf(words[j]);
        counter[index]++;
      }
      total++
    }
  }
}

var timeStamp = doc.createtime.split(' ')[0];
var dayTime  = timeStamp.split('-');
var year = dayTime[0];
var month = dayTime[1];
var day  = dayTime[2];


if (word_find.length > 0) {
  for (k = 0; k < word_find.length; k++) {
    var weather_word = weather[k];
    var count_all = counter[k];
    emit([doc.placename,year,month,day,weather_word],count_all)
  }
}
}"""

map_function_unemployment="""function (doc) {
  const split = doc.text;
  const weather = ["recession","inflation","homelessness",
  "employment","underemployment","reserve army of labour","frictional unemployment",
  "poverty","welfare","nairu","productivity","full employment","structural unemployment",
  "natural rate of unemployment","great depression","job","deindustrialization","unemployment rate",
  "labor force","deficits","labor",
  "jobless","proletariat","market-clearing","exogeny","deficit",
  "unemployment compensation","joblessness","poor","sluggish",
  "percent","gap","fall","expectations","shrank","fiscal","shortfall","pressures","easing","adjusted","unemployed",
  "costs","crisis","falling","stagnating","projected","unpopularity","consumer","slashed","rises","surge","credit",
  "estimates","growing","ebola","eliza","sharply","classical economics","forecast","significantly","demand","reducing",
  "typhoid","new classical economics","low","unexpectedly","worsened","worse","gross","stagnant","interest",
  "austrian school","slump","steadily","proportion","minimum wage law","denmark","italy","aggregate demand",
  "john maynard keynes","conceptual model","disruptive technology","behavioral economics","sticky wages",
  "efficiency wages","index","classical unemployment","involuntary unemployment","macroeconomics","poorness",
  "murray rothbard","polution","cardiovascular disease","botulism","uncomfortableness","richard vedder",
  "homemaker","alzheimers","ripoff","migraine","keynesian economics","speculativeness","pessimal",
  "business cycle","salary","supply shock","cohort","deficit spending","monetary policy",
  "interest rate","capitalist mode of production","capital accumulation","karl marx","economic rent",
  "velocity of money","self-employed","demand deposit","eviction","be broke","be reject","anxiety","depression",
  "suicide","wage slavery","job hunting","have no money","path dependence","cirrhosis","technological unemployment",
  "unemployment insurance","okun's law","search theory","pink-collar","heterogeneous agents","bounce check","daycare center",
  "world","labour market","feel stress","denominator","beveridge curve","employ","housing","bankruptcies","pensions","stimulus",
  "employers","emigration","insecurity","delinquencies","inequality","mortgage","absenteeism","vacancies","layoffs","destitution",
  "claimants","workforce","taxes","salaries","gasoline","prosperity","retrenchment","deflation","households","illiteracy","census",
  "retirees","pensioners","benefits","incapacity","entitlements","insolvency","deline","underdevelopment","recidivism","workers",
  "impoverishment","medicaid","health problem","go into debt","bureau of labor statistics","xenophobia","break computer","owe money",
  "be in debt","protectionism","study economics","barack obama","tariff","get fire","sleepless night","too much information",
  "have car accident","speed ticket","nervous breakdown","be sue","get rob","become poor","be rude","little money","be own",
  "high tax","low self esteem","division of international labor comparisons","look foolish","life of misery","file for bankruptcy",
  "work overtime","lose job","legal problem","bad job","incurable disease","terminal illness","admit defeat","dangerous job",
  "recruiter","workless","insolvencies","jobseeker","workweek","paychecks","stagflationary","pauperisation","unemployment benefits",
  "organisation for economic co-operation and development","labour economics","textile manufacturing","domestic workers",
  "youth unemployment","economic inequality","anti-work","welfare state","production possibility frontier","unemployment benefit",
  "seasonal adjustment","disposable income","life expectancy","durable goods","poverty level","infant mortality",
  "lagging indicator","sickness benefit","muddle through","infant mortality rate","social security administration",
  "wage earner","brain drain","human capital","supply-side","self-sufficiency","monetarism","trade barrier",
  "national industrial recovery act","mass production","white paper on full employment in australia","public works",
  "works progress administration","social welfare program","job guarantee"];

var word_find = [];
var counter = [];

var arr = split.toLowerCase().split(/[.,\/ -!?'"#@]/);
var i, j;
var total = 0
for (i = 0; i < arr.length; i++) {
  for (j = 0; j < weather.length; j++) {
    if (arr[i] == weather[j]) {
      var word = arr[i];
      if (word_find.includes(word) == false) {
        word_find.push(word);
        counter.push(doc.polarity);
      } else {
        var index = word_find.indexOf(words[j]);
        counter[index]++;
      }
      total++
    }
  }
}

var timeStamp = doc.createtime.split(' ')[0];
var dayTime  = timeStamp.split('-');
var year = dayTime[0];
var month = dayTime[1];
var day  = dayTime[2];


if (word_find.length > 0) {
  for (k = 0; k < word_find.length; k++) {
    var weather_word = weather[k];
    var count_all = counter[k];
    emit([doc.placename,year,month,day,weather_word],count_all)
  }
}
}"""

reduce_function_weather = """function(keys, values, rereduce) {
    if (rereduce) {
      var total = values.reduce(function(a, b) { return a + b.sum }, 0)
      var count = values.reduce(function(a, b) { return a + b.count }, 0)
        return {
            'Total_Polarity':total,
            'Count_Twitter':count,
            'Average_Polarity':total/count
        }
    } else {
        return {
            'sum': sum(values),
            'min': Math.min.apply(null, values),
            'max': Math.max.apply(null, values),
            'count': values.length,
            'sumsqr': (function() {
            var sumsqr = 0;

            values.forEach(function (value) {
                sumsqr += value * value;
            });

            return sumsqr;
            })(),
        }
    }
}"""

map_function_vaccine_date = """function (doc) {
  const split = doc.text;
  const weather = ["Pfizer","BioNTech","Oxford vaccine","Astrazeneca vaccine","COVID-19","covid-19","covid",
                  "COVID","vaccine","Vaccine","coronavirus vaccine","coronavirus"];

var word_find = [];
var counter = [];

var arr = split.split(/[.,\/ -!?'"#@]/);
var i, j;
var total = 0
for (i = 0; i < arr.length; i++) {
  for (j = 0; j < weather.length; j++) {
    if (arr[i] == weather[j]) {
      var word = arr[i];
      if (word_find.includes(word) == false) {
        word_find.push(word);
        counter.push(doc.polarity);
      } else {
        var index = word_find.indexOf(words[j]);
        counter[index]=counter[index]+doc.polarity;
      }
      total++
    }
  }
}

var timeStamp = doc.createtime.split(' ')[0];
var dayTime  = timeStamp.split('-');
var year = dayTime[0];
var month = dayTime[1];
var day  = dayTime[2];

const citylist = ["Melbourne", "Sydney","Brisbane","Perth (WA)","Canberra","Adelaide","Newcastle","Gold Coast"];

if (word_find.length > 0) {
  for (k = 0; k < word_find.length; k++) {
    var weather_word = weather[k];
    var count_all = counter[k];
    if (citylist.includes(doc.placename) == true){
      emit([year,month,day,doc.placename],count_all)
    }

  }
}
}"""

map_function_vaccine_date_sub = """function (doc) {
  const split = doc.text;
  const weather = ["Pfizer","BioNTech","Oxford vaccine","Astrazeneca vaccine","COVID-19","covid-19","covid",
                  "COVID","vaccine","Vaccine","coronavirus vaccine","coronavirus"];

var word_find = [];
var counter = [];

var arr = split.split(/[.,\/ -!?'"#@]/);
var i, j;
var total = 0
for (i = 0; i < arr.length; i++) {
  for (j = 0; j < weather.length; j++) {
    if (arr[i] == weather[j]) {
      var word = arr[i];
      if (word_find.includes(word) == false) {
        word_find.push(word);
        counter.push(doc.subjectivity);
      } else {
        var index = word_find.indexOf(words[j]);
        counter[index]=counter[index]+doc.subjectivity;
      }
      total++
    }
  }
}

var timeStamp = doc.createtime.split(' ')[0];
var dayTime  = timeStamp.split('-');
var year = dayTime[0];
var month = dayTime[1];
var day  = dayTime[2];

const citylist = ["Melbourne", "Sydney","Brisbane","Perth (WA)","Canberra","Adelaide","Newcastle","Gold Coast"];

if (word_find.length > 0) {
  for (k = 0; k < word_find.length; k++) {
    var weather_word = weather[k];
    var count_all = counter[k];
    if (citylist.includes(doc.placename) == true){
      emit([year,month,day,doc.placename],count_all)
    }

  }
}
}"""


reduce_function_vaccine = """function(keys, values, rereduce) {
    if (rereduce) {
      return{
      'sum': values.reduce(function(a, b) { return a + b.sum }, 0),
      'count': values.reduce(function(a, b) { return a + b.count }, 0),
      'average':values.reduce(function(a, b) { return a + b.sum }, 0)/values.reduce(function(a, b) { return a + b.count }, 0)
      }

    } else {
        return {
            'sum': sum(values),
            'min': Math.min.apply(null, values),
            'max': Math.max.apply(null, values),
            'count': values.length,
            'sumsqr': (function() {
            var sumsqr = 0;

            values.forEach(function (value) {
                sumsqr += value * value;
            });

            return sumsqr;
            })(),
        }
    }
}"""

map_function_vaccine_region = """function (doc) {
  const split = doc.text;
  const weather = ["Pfizer","BioNTech","Oxford vaccine","Astrazeneca vaccine","COVID-19","covid-19","covid",
                  "COVID","vaccine","Vaccine","coronavirus vaccine","coronavirus"];

var word_find = [];
var counter = [];

var arr = split.split(/[.,\/ -!?'"#@]/);
var i, j;
var total = 0
for (i = 0; i < arr.length; i++) {
  for (j = 0; j < weather.length; j++) {
    if (arr[i] == weather[j]) {
      var word = arr[i];
      if (word_find.includes(word) == false) {
        word_find.push(word);
        counter.push(doc.polarity);
      } else {
        var index = word_find.indexOf(words[j]);
        counter[index]=counter[index]+doc.polarity;
      }
      total++
    }
  }
}

var timeStamp = doc.createtime.split(' ')[0];
var dayTime  = timeStamp.split('-');
var year = dayTime[0];
var month = dayTime[1];
var day  = dayTime[2];

const citylist = ["Melbourne", "Sydney","Brisbane","Perth (WA)","Canberra","Adelaide","Newcastle","Gold Coast"];

if (word_find.length > 0) {
  for (k = 0; k < word_find.length; k++) {
    var weather_word = weather[k];
    var count_all = counter[k];
    if (citylist.includes(doc.placename) == true){
      emit([doc.placename,weather_word],count_all)
    }

  }
}
}"""

map_function_time_polarity="""function (doc) {

var timeStamp = doc.createtime.split(' ')[1];
var dayTime  = timeStamp.split(':');
var time = dayTime[0];

emit([time],doc.polarity)
}"""

map_function_time_region_polarity="""function (doc) {

var timeStamp = doc.createtime.split(' ')[1];
var dayTime  = timeStamp.split(':');
var time = dayTime[0];
const citylist = ["Melbourne", "Sydney","Brisbane","Perth (WA)","Canberra","Adelaide","Newcastle","Gold Coast"];

if (citylist.includes(doc.placename) == true){
  emit([doc.placename,time],doc.polarity)
}
}"""

map_function_time_sub="""function (doc) {

var timeStamp = doc.createtime.split(' ')[1];
var dayTime  = timeStamp.split(':');
var time = dayTime[0];

emit([time],doc.subjectivity)
}
"""

map_function_source_polarity="""function (doc) {

var timeStamp = doc.createtime.split(' ')[1];
var dayTime  = timeStamp.split(':');
var time = dayTime[0];

const sourcelist = ["Twitter for Android","Twitter for iPhone"];

if (sourcelist.includes(doc['source']) == true){
  emit([doc['source'],time],doc.polarity)
}
}"""

map_function_source_sub="""function (doc) {

var timeStamp = doc.createtime.split(' ')[1];
var dayTime  = timeStamp.split(':');
var time = dayTime[0];

const sourcelist = ["Twitter for Android","Twitter for iPhone"];

if (sourcelist.includes(doc['source']) == true){
  emit([doc['source'],time],doc.subjectivity)
}
}"""

map_function_source_region="""function (doc) {

var timeStamp = doc.createtime.split(' ')[1];
var dayTime  = timeStamp.split(':');
var time = dayTime[0];

const sourcelist = ["Twitter for Android","Twitter for iPhone"];
const citylist = ["Melbourne", "Sydney","Brisbane","Perth (WA)","Canberra","Adelaide","Newcastle","Gold Coast"];

if (citylist.includes(doc.placename) == true){
  if (sourcelist.includes(doc['source']) == true){
  emit([doc.placename,doc['source'],time],doc.polarity)
}
}

}"""

map_function_vaccine_aurin="""function (doc) {
  const split = doc.text;
  const weather = ["Pfizer","BioNTech","Oxford vaccine","Astrazeneca vaccine","COVID-19","covid-19","covid",
                  "COVID","vaccine","Vaccine","coronavirus vaccine","coronavirus"];
  const att=["positive","negative","neutral"];
var arr = split.split(/[.,\/ -!?'"#@]/);
var i, j;
var total = 0
var include = false
var key="neutral";
for (i = 0; i < arr.length; i++) {
  for (j = 0; j < weather.length; j++) {
    if (arr[i] == weather[j]) {
      include = true
      var pol = parseFloat(doc.polarity)
      if (pol<-0){
        key="negative";
      }
      else if (pol>0){
        key="positive";
      }
      total++
      break;
      break;
    }
  }
}

const citylist = ["Melbourne", "Sydney","Brisbane","Perth (WA)","Canberra","Adelaide","Newcastle","Gold Coast"];

if (include == true){
  if (citylist.includes(doc.placename) == true){
    emit([doc.placename,key],doc.polarity)
  }
}
}"""

map_function_get_unemployment_rate="""function (doc) {
  emit([doc.unemployment_rate,doc.city], doc.unemployment_rate);
}"""

map_function_get_youth_unemployment_rate="""function (doc) {
  emit([doc.youth_unemployment_rate,doc.city], doc.youth_unemployment_rate);
}"""
map_function_unemp_mentioned="""function (doc) {
  const split = doc.text;
  const weather = ["recession","inflation","homelessness",
  "employment","underemployment","reserve army of labour","frictional unemployment",
  "poverty","welfare","nairu","productivity","full employment","structural unemployment",
  "natural rate of unemployment","great depression","job","deindustrialization","unemployment rate",
  "labor force","deficits","labor",
  "jobless","proletariat","market-clearing","exogeny","deficit",
  "unemployment compensation","joblessness","poor","sluggish",
  "percent","gap","fall","expectations","shrank","fiscal","shortfall","pressures","easing","adjusted","unemployed",
  "costs","crisis","falling","stagnating","projected","unpopularity","consumer","slashed","rises","surge","credit",
  "estimates","growing","ebola","eliza","sharply","classical economics","forecast","significantly","demand","reducing",
  "typhoid","new classical economics","low","unexpectedly","worsened","worse","gross","stagnant","interest",
  "austrian school","slump","steadily","proportion","minimum wage law","denmark","italy","aggregate demand",
  "john maynard keynes","conceptual model","disruptive technology","behavioral economics","sticky wages",
  "efficiency wages","index","classical unemployment","involuntary unemployment","macroeconomics","poorness",
  "murray rothbard","polution","cardiovascular disease","botulism","uncomfortableness","richard vedder",
  "homemaker","alzheimers","ripoff","migraine","keynesian economics","speculativeness","pessimal",
  "business cycle","salary","supply shock","cohort","deficit spending","monetary policy",
  "interest rate","capitalist mode of production","capital accumulation","karl marx","economic rent",
  "velocity of money","self-employed","demand deposit","eviction","be broke","be reject","anxiety","depression",
  "suicide","wage slavery","job hunting","have no money","path dependence","cirrhosis","technological unemployment",
  "unemployment insurance","okun's law","search theory","pink-collar","heterogeneous agents","bounce check","daycare center",
  "world","labour market","feel stress","denominator","beveridge curve","employ","housing","bankruptcies","pensions","stimulus",
  "employers","emigration","insecurity","delinquencies","inequality","mortgage","absenteeism","vacancies","layoffs","destitution",
  "claimants","workforce","taxes","salaries","gasoline","prosperity","retrenchment","deflation","households","illiteracy","census",
  "retirees","pensioners","benefits","incapacity","entitlements","insolvency","deline","underdevelopment","recidivism","workers",
  "impoverishment","medicaid","health problem","go into debt","bureau of labor statistics","xenophobia","break computer","owe money",
  "be in debt","protectionism","study economics","barack obama","tariff","get fire","sleepless night","too much information",
  "have car accident","speed ticket","nervous breakdown","be sue","get rob","become poor","be rude","little money","be own",
  "high tax","low self esteem","division of international labor comparisons","look foolish","life of misery","file for bankruptcy",
  "work overtime","lose job","legal problem","bad job","incurable disease","terminal illness","admit defeat","dangerous job",
  "recruiter","workless","insolvencies","jobseeker","workweek","paychecks","stagflationary","pauperisation","unemployment benefits",
  "organisation for economic co-operation and development","labour economics","textile manufacturing","domestic workers",
  "youth unemployment","economic inequality","anti-work","welfare state","production possibility frontier","unemployment benefit",
  "seasonal adjustment","disposable income","life expectancy","durable goods","poverty level","infant mortality",
  "lagging indicator","sickness benefit","muddle through","infant mortality rate","social security administration",
  "wage earner","brain drain","human capital","supply-side","self-sufficiency","monetarism","trade barrier",
  "national industrial recovery act","mass production","white paper on full employment in australia","public works",
  "works progress administration","social welfare program","job guarantee"];

var word_find = [];
var counter = [];

var arr = split.split(/[.,\/ -!?'"#@]/);
var i, j;
var total = 0
for (i = 0; i < arr.length; i++) {
  for (j = 0; j < weather.length; j++) {
    if (arr[i] == weather[j]) {
      var word = arr[i];
      if (word_find.includes(word) == false) {
        word_find.push(word);
        counter.push(doc.polarity);
      } else {
        var index = word_find.indexOf(words[j]);
        counter[index]=counter[index]+doc.polarity;
      }
      total++
    }
  }
}

var timeStamp = doc.createtime.split(' ')[0];
var dayTime  = timeStamp.split('-');
var year = dayTime[0];
var month = dayTime[1];
var day  = dayTime[2];

const citylist = ["Melbourne", "Sydney","Brisbane","Perth (WA)","Canberra","Adelaide","Newcastle","Gold Coast"];

if (word_find.length > 0) {
  for (k = 0; k < word_find.length; k++) {
    var weather_word = weather[k];
    var count_all = counter[k];
    if (citylist.includes(doc.placename) == true){
      emit([weather_word,doc.placename],count_all)
    }

  }
}
}"""

map_function_unemp_polarity="""function (doc) {
  const split = doc.text;
  const weather = ["recession","inflation","homelessness",
  "employment","underemployment","reserve army of labour","frictional unemployment",
  "poverty","welfare","nairu","productivity","full employment","structural unemployment",
  "natural rate of unemployment","great depression","job","deindustrialization","unemployment rate",
  "labor force","deficits","labor",
  "jobless","proletariat","market-clearing","exogeny","deficit",
  "unemployment compensation","joblessness","poor","sluggish",
  "percent","gap","fall","expectations","shrank","fiscal","shortfall","pressures","easing","adjusted","unemployed",
  "costs","crisis","falling","stagnating","projected","unpopularity","consumer","slashed","rises","surge","credit",
  "estimates","growing","ebola","eliza","sharply","classical economics","forecast","significantly","demand","reducing",
  "typhoid","new classical economics","low","unexpectedly","worsened","worse","gross","stagnant","interest",
  "austrian school","slump","steadily","proportion","minimum wage law","denmark","italy","aggregate demand",
  "john maynard keynes","conceptual model","disruptive technology","behavioral economics","sticky wages",
  "efficiency wages","index","classical unemployment","involuntary unemployment","macroeconomics","poorness",
  "murray rothbard","polution","cardiovascular disease","botulism","uncomfortableness","richard vedder",
  "homemaker","alzheimers","ripoff","migraine","keynesian economics","speculativeness","pessimal",
  "business cycle","salary","supply shock","cohort","deficit spending","monetary policy",
  "interest rate","capitalist mode of production","capital accumulation","karl marx","economic rent",
  "velocity of money","self-employed","demand deposit","eviction","be broke","be reject","anxiety","depression",
  "suicide","wage slavery","job hunting","have no money","path dependence","cirrhosis","technological unemployment",
  "unemployment insurance","okun's law","search theory","pink-collar","heterogeneous agents","bounce check","daycare center",
  "world","labour market","feel stress","denominator","beveridge curve","employ","housing","bankruptcies","pensions","stimulus",
  "employers","emigration","insecurity","delinquencies","inequality","mortgage","absenteeism","vacancies","layoffs","destitution",
  "claimants","workforce","taxes","salaries","gasoline","prosperity","retrenchment","deflation","households","illiteracy","census",
  "retirees","pensioners","benefits","incapacity","entitlements","insolvency","deline","underdevelopment","recidivism","workers",
  "impoverishment","medicaid","health problem","go into debt","bureau of labor statistics","xenophobia","break computer","owe money",
  "be in debt","protectionism","study economics","barack obama","tariff","get fire","sleepless night","too much information",
  "have car accident","speed ticket","nervous breakdown","be sue","get rob","become poor","be rude","little money","be own",
  "high tax","low self esteem","division of international labor comparisons","look foolish","life of misery","file for bankruptcy",
  "work overtime","lose job","legal problem","bad job","incurable disease","terminal illness","admit defeat","dangerous job",
  "recruiter","workless","insolvencies","jobseeker","workweek","paychecks","stagflationary","pauperisation","unemployment benefits",
  "organisation for economic co-operation and development","labour economics","textile manufacturing","domestic workers",
  "youth unemployment","economic inequality","anti-work","welfare state","production possibility frontier","unemployment benefit",
  "seasonal adjustment","disposable income","life expectancy","durable goods","poverty level","infant mortality",
  "lagging indicator","sickness benefit","muddle through","infant mortality rate","social security administration",
  "wage earner","brain drain","human capital","supply-side","self-sufficiency","monetarism","trade barrier",
  "national industrial recovery act","mass production","white paper on full employment in australia","public works",
  "works progress administration","social welfare program","job guarantee"];


var word_find = [];
var counter = [];

var arr = split.split(/[.,\/ -!?'"#@]/);
var i, j;
var total = 0
for (i = 0; i < arr.length; i++) {
  for (j = 0; j < weather.length; j++) {
    if (arr[i] == weather[j]) {
      var word = arr[i];
      if (word_find.includes(word) == false) {
        word_find.push(word);
        counter.push(doc.polarity);
      } else {
        var index = word_find.indexOf(words[j]);
        counter[index]=counter[index]+doc.polarity;
      }
      total++
    }
  }
}

var timeStamp = doc.createtime.split(' ')[0];
var dayTime  = timeStamp.split('-');
var year = dayTime[0];
var month = dayTime[1];
var day  = dayTime[2];

const citylist = ["Melbourne", "Sydney","Brisbane","Perth (WA)","Canberra","Adelaide","Newcastle","Gold Coast"];

if (word_find.length > 0) {
  for (k = 0; k < word_find.length; k++) {
    var weather_word = weather[k];
    var count_all = counter[k];
    if (citylist.includes(doc.placename) == true){
      emit([year,month,day,doc.placename],count_all)
    }

  }
}
}"""

map_function_unemp_region="""function (doc) {
  const split = doc.text;
  const weather = ["recession","inflation","homelessness",
  "employment","underemployment","reserve army of labour","frictional unemployment",
  "poverty","welfare","nairu","productivity","full employment","structural unemployment",
  "natural rate of unemployment","great depression","job","deindustrialization","unemployment rate",
  "labor force","deficits","labor",
  "jobless","proletariat","market-clearing","exogeny","deficit",
  "unemployment compensation","joblessness","poor","sluggish",
  "percent","gap","fall","expectations","shrank","fiscal","shortfall","pressures","easing","adjusted","unemployed",
  "costs","crisis","falling","stagnating","projected","unpopularity","consumer","slashed","rises","surge","credit",
  "estimates","growing","ebola","eliza","sharply","classical economics","forecast","significantly","demand","reducing",
  "typhoid","new classical economics","low","unexpectedly","worsened","worse","gross","stagnant","interest",
  "austrian school","slump","steadily","proportion","minimum wage law","denmark","italy","aggregate demand",
  "john maynard keynes","conceptual model","disruptive technology","behavioral economics","sticky wages",
  "efficiency wages","index","classical unemployment","involuntary unemployment","macroeconomics","poorness",
  "murray rothbard","polution","cardiovascular disease","botulism","uncomfortableness","richard vedder",
  "homemaker","alzheimers","ripoff","migraine","keynesian economics","speculativeness","pessimal",
  "business cycle","salary","supply shock","cohort","deficit spending","monetary policy",
  "interest rate","capitalist mode of production","capital accumulation","karl marx","economic rent",
  "velocity of money","self-employed","demand deposit","eviction","be broke","be reject","anxiety","depression",
  "suicide","wage slavery","job hunting","have no money","path dependence","cirrhosis","technological unemployment",
  "unemployment insurance","okun's law","search theory","pink-collar","heterogeneous agents","bounce check","daycare center",
  "world","labour market","feel stress","denominator","beveridge curve","employ","housing","bankruptcies","pensions","stimulus",
  "employers","emigration","insecurity","delinquencies","inequality","mortgage","absenteeism","vacancies","layoffs","destitution",
  "claimants","workforce","taxes","salaries","gasoline","prosperity","retrenchment","deflation","households","illiteracy","census",
  "retirees","pensioners","benefits","incapacity","entitlements","insolvency","deline","underdevelopment","recidivism","workers",
  "impoverishment","medicaid","health problem","go into debt","bureau of labor statistics","xenophobia","break computer","owe money",
  "be in debt","protectionism","study economics","barack obama","tariff","get fire","sleepless night","too much information",
  "have car accident","speed ticket","nervous breakdown","be sue","get rob","become poor","be rude","little money","be own",
  "high tax","low self esteem","division of international labor comparisons","look foolish","life of misery","file for bankruptcy",
  "work overtime","lose job","legal problem","bad job","incurable disease","terminal illness","admit defeat","dangerous job",
  "recruiter","workless","insolvencies","jobseeker","workweek","paychecks","stagflationary","pauperisation","unemployment benefits",
  "organisation for economic co-operation and development","labour economics","textile manufacturing","domestic workers",
  "youth unemployment","economic inequality","anti-work","welfare state","production possibility frontier","unemployment benefit",
  "seasonal adjustment","disposable income","life expectancy","durable goods","poverty level","infant mortality",
  "lagging indicator","sickness benefit","muddle through","infant mortality rate","social security administration",
  "wage earner","brain drain","human capital","supply-side","self-sufficiency","monetarism","trade barrier",
  "national industrial recovery act","mass production","white paper on full employment in australia","public works",
  "works progress administration","social welfare program","job guarantee"];

var word_find = [];
var counter = [];

var arr = split.split(/[.,\/ -!?'"#@]/);
var i, j;
var total = 0
for (i = 0; i < arr.length; i++) {
  for (j = 0; j < weather.length; j++) {
    if (arr[i] == weather[j]) {
      var word = arr[i];
      if (word_find.includes(word) == false) {
        word_find.push(word);
        counter.push(doc.polarity);
      } else {
        var index = word_find.indexOf(words[j]);
        counter[index]=counter[index]+doc.polarity;
      }
      total++
    }
  }
}

var timeStamp = doc.createtime.split(' ')[0];
var dayTime  = timeStamp.split('-');
var year = dayTime[0];
var month = dayTime[1];
var day  = dayTime[2];

const citylist = ["Melbourne", "Sydney","Brisbane","Perth (WA)","Canberra","Adelaide","Newcastle","Gold Coast"];

if (word_find.length > 0) {
  for (k = 0; k < word_find.length; k++) {
    var weather_word = weather[k];
    var count_all = counter[k];
    if (citylist.includes(doc.placename) == true){
      emit([doc.placename,weather_word],count_all)
    }

  }
}
}"""

map_function_unemp_sub="""function (doc) {
  const split = doc.text;
  const weather = ["recession","inflation","homelessness",
  "employment","underemployment","reserve army of labour","frictional unemployment",
  "poverty","welfare","nairu","productivity","full employment","structural unemployment",
  "natural rate of unemployment","great depression","job","deindustrialization","unemployment rate",
  "labor force","deficits","labor",
  "jobless","proletariat","market-clearing","exogeny","deficit",
  "unemployment compensation","joblessness","poor","sluggish",
  "percent","gap","fall","expectations","shrank","fiscal","shortfall","pressures","easing","adjusted","unemployed",
  "costs","crisis","falling","stagnating","projected","unpopularity","consumer","slashed","rises","surge","credit",
  "estimates","growing","ebola","eliza","sharply","classical economics","forecast","significantly","demand","reducing",
  "typhoid","new classical economics","low","unexpectedly","worsened","worse","gross","stagnant","interest",
  "austrian school","slump","steadily","proportion","minimum wage law","denmark","italy","aggregate demand",
  "john maynard keynes","conceptual model","disruptive technology","behavioral economics","sticky wages",
  "efficiency wages","index","classical unemployment","involuntary unemployment","macroeconomics","poorness",
  "murray rothbard","polution","cardiovascular disease","botulism","uncomfortableness","richard vedder",
  "homemaker","alzheimers","ripoff","migraine","keynesian economics","speculativeness","pessimal",
  "business cycle","salary","supply shock","cohort","deficit spending","monetary policy",
  "interest rate","capitalist mode of production","capital accumulation","karl marx","economic rent",
  "velocity of money","self-employed","demand deposit","eviction","be broke","be reject","anxiety","depression",
  "suicide","wage slavery","job hunting","have no money","path dependence","cirrhosis","technological unemployment",
  "unemployment insurance","okun's law","search theory","pink-collar","heterogeneous agents","bounce check","daycare center",
  "world","labour market","feel stress","denominator","beveridge curve","employ","housing","bankruptcies","pensions","stimulus",
  "employers","emigration","insecurity","delinquencies","inequality","mortgage","absenteeism","vacancies","layoffs","destitution",
  "claimants","workforce","taxes","salaries","gasoline","prosperity","retrenchment","deflation","households","illiteracy","census",
  "retirees","pensioners","benefits","incapacity","entitlements","insolvency","deline","underdevelopment","recidivism","workers",
  "impoverishment","medicaid","health problem","go into debt","bureau of labor statistics","xenophobia","break computer","owe money",
  "be in debt","protectionism","study economics","barack obama","tariff","get fire","sleepless night","too much information",
  "have car accident","speed ticket","nervous breakdown","be sue","get rob","become poor","be rude","little money","be own",
  "high tax","low self esteem","division of international labor comparisons","look foolish","life of misery","file for bankruptcy",
  "work overtime","lose job","legal problem","bad job","incurable disease","terminal illness","admit defeat","dangerous job",
  "recruiter","workless","insolvencies","jobseeker","workweek","paychecks","stagflationary","pauperisation","unemployment benefits",
  "organisation for economic co-operation and development","labour economics","textile manufacturing","domestic workers",
  "youth unemployment","economic inequality","anti-work","welfare state","production possibility frontier","unemployment benefit",
  "seasonal adjustment","disposable income","life expectancy","durable goods","poverty level","infant mortality",
  "lagging indicator","sickness benefit","muddle through","infant mortality rate","social security administration",
  "wage earner","brain drain","human capital","supply-side","self-sufficiency","monetarism","trade barrier",
  "national industrial recovery act","mass production","white paper on full employment in australia","public works",
  "works progress administration","social welfare program","job guarantee"];

var word_find = [];
var counter = [];

var arr = split.split(/[.,\/ -!?'"#@]/);
var i, j;
var total = 0
for (i = 0; i < arr.length; i++) {
  for (j = 0; j < weather.length; j++) {
    if (arr[i] == weather[j]) {
      var word = arr[i];
      if (word_find.includes(word) == false) {
        word_find.push(word);
        counter.push(doc.subjectivity);
      } else {
        var index = word_find.indexOf(words[j]);
        counter[index]=counter[index]+doc.subjectivity;
      }
      total++
    }
  }
}

var timeStamp = doc.createtime.split(' ')[0];
var dayTime  = timeStamp.split('-');
var year = dayTime[0];
var month = dayTime[1];
var day  = dayTime[2];

const citylist = ["Melbourne", "Sydney","Brisbane","Perth (WA)","Canberra","Adelaide","Newcastle","Gold Coast"];

if (word_find.length > 0) {
  for (k = 0; k < word_find.length; k++) {
    var weather_word = weather[k];
    var count_all = counter[k];
    if (citylist.includes(doc.placename) == true){
      emit([year,month,day,doc.placename],count_all)
    }

  }
}
}"""

map_function_unemployment_analysis="""function (doc) {
  const split = doc.text;
  const weather = ["recession","inflation","homelessness",
  "employment","underemployment","reserve army of labour","frictional unemployment",
  "poverty","welfare","nairu","productivity","full employment","structural unemployment",
  "natural rate of unemployment","great depression","job","deindustrialization","unemployment rate",
  "labor force","deficits","labor",
  "jobless","proletariat","market-clearing","exogeny","deficit",
  "unemployment compensation","joblessness","poor","sluggish",
  "percent","gap","fall","expectations","shrank","fiscal","shortfall","pressures","easing","adjusted","unemployed",
  "costs","crisis","falling","stagnating","projected","unpopularity","consumer","slashed","rises","surge","credit",
  "estimates","growing","ebola","eliza","sharply","classical economics","forecast","significantly","demand","reducing",
  "typhoid","new classical economics","low","unexpectedly","worsened","worse","gross","stagnant","interest",
  "austrian school","slump","steadily","proportion","minimum wage law","denmark","italy","aggregate demand",
  "john maynard keynes","conceptual model","disruptive technology","behavioral economics","sticky wages",
  "efficiency wages","index","classical unemployment","involuntary unemployment","macroeconomics","poorness",
  "murray rothbard","polution","cardiovascular disease","botulism","uncomfortableness","richard vedder",
  "homemaker","alzheimers","ripoff","migraine","keynesian economics","speculativeness","pessimal",
  "business cycle","salary","supply shock","cohort","deficit spending","monetary policy",
  "interest rate","capitalist mode of production","capital accumulation","karl marx","economic rent",
  "velocity of money","self-employed","demand deposit","eviction","be broke","be reject","anxiety","depression",
  "suicide","wage slavery","job hunting","have no money","path dependence","cirrhosis","technological unemployment",
  "unemployment insurance","okun's law","search theory","pink-collar","heterogeneous agents","bounce check","daycare center",
  "world","labour market","feel stress","denominator","beveridge curve","employ","housing","bankruptcies","pensions","stimulus",
  "employers","emigration","insecurity","delinquencies","inequality","mortgage","absenteeism","vacancies","layoffs","destitution",
  "claimants","workforce","taxes","salaries","gasoline","prosperity","retrenchment","deflation","households","illiteracy","census",
  "retirees","pensioners","benefits","incapacity","entitlements","insolvency","deline","underdevelopment","recidivism","workers",
  "impoverishment","medicaid","health problem","go into debt","bureau of labor statistics","xenophobia","break computer","owe money",
  "be in debt","protectionism","study economics","barack obama","tariff","get fire","sleepless night","too much information",
  "have car accident","speed ticket","nervous breakdown","be sue","get rob","become poor","be rude","little money","be own",
  "high tax","low self esteem","division of international labor comparisons","look foolish","life of misery","file for bankruptcy",
  "work overtime","lose job","legal problem","bad job","incurable disease","terminal illness","admit defeat","dangerous job",
  "recruiter","workless","insolvencies","jobseeker","workweek","paychecks","stagflationary","pauperisation","unemployment benefits",
  "organisation for economic co-operation and development","labour economics","textile manufacturing","domestic workers",
  "youth unemployment","economic inequality","anti-work","welfare state","production possibility frontier","unemployment benefit",
  "seasonal adjustment","disposable income","life expectancy","durable goods","poverty level","infant mortality",
  "lagging indicator","sickness benefit","muddle through","infant mortality rate","social security administration",
  "wage earner","brain drain","human capital","supply-side","self-sufficiency","monetarism","trade barrier",
  "national industrial recovery act","mass production","white paper on full employment in australia","public works",
  "works progress administration","social welfare program","job guarantee"];

var word_find = [];
var counter = [];

var arr = split.toLowerCase().split(/[.,\/ -!?'"#@]/);
var i, j;
var total = 0
for (i = 0; i < arr.length; i++) {
  for (j = 0; j < weather.length; j++) {
    if (arr[i] == weather[j]) {
      var word = arr[i];
      if (word_find.includes(word) == false) {
        word_find.push(word);
        counter.push(doc.polarity);
      } else {
        var index = word_find.indexOf(words[j]);
        counter[index]++;
      }
      total++
    }
  }
}

var timeStamp = doc.createtime.split(' ')[0];
var dayTime  = timeStamp.split('-');
var year = dayTime[0];
var month = dayTime[1];
var day  = dayTime[2];

const citylist = ["Melbourne", "Sydney","Brisbane","Perth (WA)","Canberra","Adelaide","Newcastle","Gold Coast"];

if (word_find.length > 0) {
  for (k = 0; k < word_find.length; k++) {
    var weather_word = weather[k];
    var count_all = counter[k];
    if (citylist.includes(doc.placename) == true){
      emit([doc.placename,year,month,day,weather_word],count_all)
    }

  }
}
}"""

map_function_time_date="""function (doc) {

var timeStamp = doc.createtime.split(' ')[1];
var dayTime  = timeStamp.split(':');
var timedate = doc.createtime.split(' ')[0];
var time = dayTime[0];

emit([timedate,time],doc.polarity)
}"""

design_doc = 'climate_analysis'
view_weather = "climate"
createView(dbConn=db, designDoc=design_doc, viewName=view_weather, mapFunction=map_function_weather,
           reduceFunction=reduce_function_vaccine)

view_vaccine_date = "vaccine_date"
design_doc_vaccine_date = "vaccine_analysis"
createView(dbConn=db, designDoc=design_doc_vaccine_date, viewName=view_vaccine_date,
           mapFunction=map_function_vaccine_date, reduceFunction=reduce_function_vaccine)

view_vaccine_date_sub = "vaccine_date_sub"
design_doc_vaccine_date_sub = "vaccine_analysis"
addView(db=db, designDoc=design_doc_vaccine_date_sub, viewName=view_vaccine_date_sub,
           mapFunction=map_function_vaccine_date_sub, reduceFunction=reduce_function_vaccine)

view_vaccine_region = "vaccine_region"
design_doc_vaccine_region = "vaccine_analysis"
addView(db=db, designDoc=design_doc_vaccine_region, viewName=view_vaccine_region,
           mapFunction=map_function_vaccine_region, reduceFunction=reduce_function_vaccine)

view_vaccine_aurin = "vaccine_aurin"
design_doc_vaccine_region = "vaccine_analysis"
addView(db=db, designDoc=design_doc_vaccine_region, viewName=view_vaccine_aurin,
           mapFunction=map_function_vaccine_aurin, reduceFunction=reduce_function_vaccine)


view_time_polarity = "time_polarity"
design_doc_time = "time_analysis"
createView(dbConn=db, designDoc=design_doc_time, viewName=view_time_polarity,
           mapFunction=map_function_time_polarity, reduceFunction=reduce_function_vaccine)

view_time_date = "time_date"
#design_doc_vaccine = "time_analysis"
addView(db=db, designDoc=design_doc_time, viewName=view_time_date,
           mapFunction=map_function_time_date, reduceFunction=reduce_function_vaccine)

view_time_region_polarity = "time_region_polarity"
#design_doc_vaccine = "time_analysis"
addView(db=db, designDoc=design_doc_time, viewName=view_time_region_polarity,
           mapFunction=map_function_time_region_polarity, reduceFunction=reduce_function_vaccine)

view_time_sub = "time_sub"
#design_doc_vaccine_region = "vaccine_analysis"
addView(db=db, designDoc=design_doc_time, viewName=view_time_sub,
           mapFunction=map_function_time_sub, reduceFunction=reduce_function_vaccine)

view_source_polarity = "source_polarity"
design_doc_source = "source_analysis"
createView(dbConn=db, designDoc=design_doc_source, viewName=view_source_polarity,
           mapFunction=map_function_source_polarity, reduceFunction=reduce_function_vaccine)

view_source_sub = "source_sub"
#design_doc_vaccine_region = "vaccine_analysis"
addView(db=db, designDoc=design_doc_source, viewName=view_source_sub,
           mapFunction=map_function_source_sub, reduceFunction=reduce_function_vaccine)

view_source_region = "source_region"
#design_doc_vaccine_region = "vaccine_analysis"
addView(db=db, designDoc=design_doc_source, viewName=view_source_region,
           mapFunction=map_function_source_region, reduceFunction=reduce_function_vaccine)

view_unemp_mentioned= "unemp_mentioned"
design_doc_unemp = "unemployment_analysis"
createView(dbConn=db, designDoc=design_doc_unemp, viewName=view_unemp_mentioned,
           mapFunction=map_function_unemp_mentioned, reduceFunction=reduce_function_vaccine)

view_unemp_polarity = "unemp_polarity"
#design_doc_vaccine_region = "vaccine_analysis"
addView(db=db, designDoc=design_doc_unemp, viewName=view_unemp_polarity,
           mapFunction=map_function_unemp_polarity, reduceFunction=reduce_function_vaccine)

view_unemp_sub = "unemp_sub"
#design_doc_vaccine_region = "vaccine_analysis"
addView(db=db, designDoc=design_doc_unemp, viewName=view_unemp_sub,
           mapFunction=map_function_unemp_sub, reduceFunction=reduce_function_vaccine)

view_unemp_region = "unemp_region"
#design_doc_vaccine_region = "vaccine_analysis"
addView(db=db, designDoc=design_doc_unemp, viewName=view_unemp_region,
           mapFunction=map_function_unemp_region, reduceFunction=reduce_function_vaccine)

view_unemployment_analysis = "unemployment_analysis"
#design_doc_vaccine_region = "vaccine_analysis"
addView(db=db, designDoc=design_doc_unemp, viewName=view_unemployment_analysis,
           mapFunction=map_function_unemployment_analysis, reduceFunction=reduce_function_vaccine)
