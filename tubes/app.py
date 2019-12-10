from flask import Flask, render_template, request, jsonify
import model_dss as model
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def temp_respon():
    data = request.get_json(force=True)
    if (data['username'] == 'jeffry') & (data['password'] == "jeffrykhosasi"):
        return jsonify(result="mantepbro")
    else:
        return jsonify(result="salahbro")

@app.route('/dashboard', methods=['GET'])
def get_dashboard():
    model.df = model.pd.read_csv("../bank/bank (copy).csv")
    model.number_customer = model.df.shape[0]
    model.annual_balance = model.df['balance'].mean(axis=0)
    model.cust_joined = model.df[model.df['y'] == 'yes'].shape[0]
    model.percent_cust_joined = round((model.cust_joined / model.number_customer) * 100, 2)
    model.map_month = {'jan': model.df[model.df['y'] == 'yes']['month'].value_counts()['jan'],
                 'feb': model.df[model.df['y'] == 'yes']['month'].value_counts()['feb'],
                 'mar': model.df[model.df['y'] == 'yes']['month'].value_counts()['mar'],
                 'apr': model.df[model.df['y'] == 'yes']['month'].value_counts()['apr'],
                 'may': model.df[model.df['y'] == 'yes']['month'].value_counts()['may'],
                 'jun': model.df[model.df['y'] == 'yes']['month'].value_counts()['jun'],
                 'jul': model.df[model.df['y'] == 'yes']['month'].value_counts()['jul'],
                 'aug': model.df[model.df['y'] == 'yes']['month'].value_counts()['aug'],
                 'sep': model.df[model.df['y'] == 'yes']['month'].value_counts()['sep'],
                 'oct': model.df[model.df['y'] == 'yes']['month'].value_counts()['oct'],
                 'nov': model.df[model.df['y'] == 'yes']['month'].value_counts()['nov'],
                 'dec': model.df[model.df['y'] == 'yes']['month'].value_counts()['dec']}
    model.last_camp = model.df['poutcome'].value_counts()

    return render_template("dashboard.html", number_cust=model.number_customer,
                           annual_balance=round(model.annual_balance, 2),
                           percent_joined=model.percent_cust_joined,
                           month=model.map_month, last_camp=model.last_camp)

@app.route('/dss', methods=['POST'])
def get_dss():
    data = request.get_json(force=True)

    data.update((x, [y]) for x, y in data.items())
    data_df = model.pd.DataFrame.from_dict(data)
    print(data_df.dtypes)

    result = model.model_train.predict_proba(data_df)[:,1]

    return jsonify(results=result[0])


if __name__ == '__main__':
    app.run()
