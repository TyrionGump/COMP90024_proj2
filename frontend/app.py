from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from datetime import timedelta
import utils_source
import utils_time
import utils_vaccine

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


@app.route('/')
def hello_world():
    return render_template('main.html')


@app.route('/main.html', methods=['GET', 'POST'])
def main_page():
    return render_template('main.html')


@app.route('/language.html', methods=['GET', 'POST'])
def language():
    return render_template('language.html')


@app.route('/source.html', methods=['GET', 'POST'])
def source():
    return render_template('source.html')


@app.route('/period.html', methods=['GET', 'POST'])
def period():
    return render_template('period.html')


@app.route('/vaccine.html', methods=['GET', 'POST'])
def vaccine():
    return render_template('vaccine.html')


# 1 -------------------------------------------------------------- Language 部分 start
@app.route('/language/l1')
def get_language_l1_data():
    language_l1_data = {'Sydney': [{'name': 'english', 'value': 1231},
                                   {'name': 'chinese', 'value': 2412},
                                   {'name': 'spanish', 'value': 234}],
                        'Melbourne': [{'name': 'english', 'value': 4562},
                                      {'name': 'chinese', 'value': 3252},
                                      {'name': 'spanish', 'value': 344}],
                        'Brisbane': [{'name': 'english', 'value': 1341},
                                     {'name': 'chinese', 'value': 2212},
                                     {'name': 'spanish', 'value': 2254}],
                        'Perth': [{'name': 'english', 'value': 2131},
                                  {'name': 'chinese', 'value': 1412},
                                  {'name': 'spanish', 'value': 634}],
                        'Adelaide': [{'name': 'english', 'value': 1435},
                                     {'name': 'chinese', 'value': 6745},
                                     {'name': 'spanish', 'value': 42}],
                        'GoldCoast': [{'name': 'english', 'value': 346},
                                      {'name': 'chinese', 'value': 653},
                                      {'name': 'spanish', 'value': 452}],
                        'Canberra': [{'name': 'english', 'value': 456},
                                     {'name': 'chinese', 'value': 3465},
                                     {'name': 'spanish', 'value': 6544}],
                        'Newcastle': [{'name': 'english', 'value': 3231},
                                      {'name': 'chinese', 'value': 9756},
                                      {'name': 'spanish', 'value': 246}]}
    return jsonify(language_l1_data)


@app.route('/language/l2')
def get_language_l2_data():
    language_l2_data = {'legend': ['score_1', 'score_2'],
                        'xAxis': ['Chinese', 'English', 'Spanish', 'Germany'],
                        'data': [[100, 200, 234, 567], [200, 100, 123, 145]]}
    return jsonify(language_l2_data)


@app.route('/language/c1')
def get_language_c1_scatter_data():
    language_c1_scatter_data = {'data_name': 'android',
                                'data': [{'name': 'melbourne', 'value': [144.96316, -37.81422, [15000, 20000]]},
                                         {'name': 'brisbane', 'value': [153.021072, -27.470125, [1000, 2000]]}]}
    return jsonify(language_c1_scatter_data)


@app.route('/language/r2', methods=['GET', 'POST'])
def get_language_r2_data():
    city_name = request.values.get("name")
    language_r2_data = {'Sydney': [{'name': 'Yanhao', 'value': 123214},
                                {'name': 'Cindy', 'value': 23545},
                                {'name': 'asdasfqf', 'value': 134424}],
                     'Melbourne': [{'name': 'Yanhao', 'value': 1214},
                                   {'name': 'Cindy', 'value': 235535},
                                   {'name': 'asdasfqf', 'value': 12424}],
                     'Brisbane': [{'name': 'Yanhao', 'value': 123214},
                                  {'name': 'Cindy', 'value': 235235},
                                  {'name': 'asdasfqf', 'value': 12424}],
                     'Perth': [{'name': 'Yanhao', 'value': 123214},
                               {'name': 'Cindy', 'value': 235425},
                               {'name': 'asdasfqf', 'value': 124344}],
                     'Adelaide': [{'name': 'Yanhao', 'value': 123214},
                                  {'name': 'Cindy', 'value': 232345},
                                  {'name': 'asdasfqf', 'value': 123424}],
                     'GoldCoast': [{'name': 'Yanhao', 'value': 123214},
                                   {'name': 'Cindy', 'value': 223445},
                                   {'name': 'asdasfqf', 'value': 12424}],
                     'Canberra': [{'name': 'Yanhao', 'value': 123212314},
                                  {'name': 'Cindy', 'value': 23535},
                                  {'name': 'asdasfqf', 'value': 12424}],
                     'Newcastle': [{'name': 'Yanhao', 'value': 124214},
                                   {'name': 'Cindy', 'value': 2354515},
                                   {'name': 'asdasfqf', 'value': 12424}]
                     }

    return jsonify(language_r2_data)


# 1 -------------------------------------------------------------- Language 部分 end

# 2 -------------------------------------------------------------- Source 部分 start

@app.route('/source/l1')
def get_source_l1_data():
    source_l1_data = {'legend': ['Android', 'IOS'], 'xAxis': [str(i).zfill(2) for i in range(24)],
                      'data': utils_source.source_time_plot()}
    return jsonify(source_l1_data)


@app.route('/source/l2')
def get_source_l2_data():
    source_l2_data = {'legend': ['polarity', 'subjectivity'], 'xAxis': ['Android', 'IOS'],
                      'data': utils_source.source_polarity_subjectivity()}
    return jsonify(source_l2_data)


@app.route('/source/c12')
def get_source_c12_scatter_data():
    # 前一个IOS后一个android.
    android_data, ios_data = utils_source.source_region_pol()
    source_c12_scatter_data = {'android': android_data, 'ios': ios_data}
    return jsonify(source_c12_scatter_data)


@app.route('/source/r1')
def get_source_r1_data():
    source_r1_data = {'legend': ['Android', 'IOS'],
                      'yAxis': ['Sydney', 'Melbourne', 'Brisbane', 'Perth (WA)', 'Adelaide',
                                'Gold Coast', 'Canberra', 'Newcastle'],
                      'data': utils_source.source_region_percentage()}
    return jsonify(source_r1_data)


@app.route('/source/r2', methods=['GET', 'POST'])
def get_source_r2_data():
    source_r2_original_data = utils_source.source_cloud()
    source_r2_data = {'android': source_r2_original_data[0]['Twitter for Android'],
                      'ios': source_r2_original_data[1]['Twitter for iPhone']
                      }

    return jsonify(source_r2_data)


# 2 -------------------------------------------------------------- Source 部分 end

# 3 -------------------------------------------------------------- Period 部分 start
@app.route('/period/l1')
def get_period_l1_data():
    period_l1_data = {'xAxis': [str(i).zfill(2) for i in range(24)],
                      'data': utils_time.time_count_trend()}
    return jsonify(period_l1_data)


@app.route('/period/l2')
def get_period_l2_data():
    period_l2_data = {'legend': ['polarity', 'subjective'],
                      'xAxis': [str(i).zfill(2) for i in range(24)],
                      'data': utils_time.time_sub_pol_trend()}
    return jsonify(period_l2_data)


@app.route('/period/c1')
def get_period_c1_scatter_data():
    period_c1_scatter_data = {'timeline': [str(i).zfill(2) for i in range(24)],
                              'data': utils_time.time_map_24()}
    return jsonify(period_c1_scatter_data)


@app.route('/period/r1')
def get_period_r1_data():
    period_r1_data = {'periods': [str(i).zfill(2) for i in range(24)],
                      'xAxis': ['Sydney', 'Melbourne', 'Brisbane', 'Perth (WA)', 'Adelaide',
                                'Gold Coast', 'Canberra', 'Newcastle'],
                      'data': utils_time.time_region_count_percent_plot()}
    return jsonify(period_r1_data)


@app.route('/period/r2', methods=['GET', 'POST'])
def get_period_r2_data():
    period_r2_data = utils_time.time_cloud()

    return jsonify(period_r2_data)


# 3 -------------------------------------------------------------- Period 部分 end

# 4 -------------------------------------------------------------- Vaccine 部分 start
@app.route('/vaccine/l1')
def get_vaccine_l1_data():
    vaccine_l1_original_date = utils_vaccine.vaccine_date_count()
    vaccine_l1_data = {'xAxis': vaccine_l1_original_date[0],
                       'data': vaccine_l1_original_date[1]}
    return jsonify(vaccine_l1_data)


@app.route('/vaccine/l2')
def get_vaccine_l2_data():
    vaccine_l2_original_data = utils_vaccine.vaccine_date_polarity_sub()
    source_l2_data = {'legend': ['polarity', 'subjective'],
                      'xAxis': vaccine_l2_original_data[0],
                      'data': [vaccine_l2_original_data[1], vaccine_l2_original_data[2]]}
    return jsonify(source_l2_data)

@app.route('/vaccine/c1')
def get_vaccine_c1_scatter_data():
    vaccine_c1_scatter_data = {'data_name': 'Average polarity about vaccine',
                               'data': utils_vaccine.vaccine_map()}
    return jsonify(vaccine_c1_scatter_data)

@app.route('/vaccine/r1')
def get_vaccine_r1_data():
    vaccine_r1_data = {'legend': ['Question 1 Disagree', 'Question 2 Disagree',
                                  'Question 1 Neutral', 'Question 1 Agree',
                                  'Question 2 Neutral', 'Question 2 Agree'],
                       'data':utils_vaccine.vaccine_aurin_compare()}
    return jsonify(vaccine_r1_data)

@app.route('/vaccine/r2', methods=['GET', 'POST'])
def get_vaccine_r2_data():
    vaccine_r2_data = utils_vaccine.vaccine_cloud()

    return jsonify(vaccine_r2_data)
# 4 -------------------------------------------------------------- Vaccine 部分 end

if __name__ == '__main__':
    app.run()
