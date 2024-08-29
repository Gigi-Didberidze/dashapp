import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

data_path = "https://raw.githubusercontent.com/Gigi-Didberidze/dashapp/master/data/combined_df.csv"

combined_df = pd.read_csv(data_path)
print(combined_df)


app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.Div([
        html.H1(
            "Missing Data Visualizations",
            style={'textAlign': 'center', 'marginBottom': '30px'}
        ),
        dcc.Tabs([
            dcc.Tab(label='application_train', children=[
                dcc.Graph(
                    figure=px.line(
                        combined_df[combined_df['DataFrame'] == 'application_train'],
                        x='Column Name',
                        y='Percentage Missing',
                        title='application_train',
                        labels={'Percentage Missing': 'Percentage of Missing Values'}
                    ),
                    style={'height': 550}
                )
            ]),
            dcc.Tab(label='previous_application', children=[
                dcc.Graph(
                    figure=px.line(
                        combined_df[combined_df['DataFrame'] == 'previous_application'],
                        x='Column Name',
                        y='Percentage Missing',
                        title='previous_application',
                        labels={'Percentage Missing': 'Percentage of Missing Values'}
                    )
                )
            ]),
            dcc.Tab(label='bureau', children=[
                dcc.Graph(
                    figure=px.line(
                        combined_df[combined_df['DataFrame'] == 'bureau'],
                        x='Column Name',
                        y='Percentage Missing',
                        title='bureau',
                        labels={'Percentage Missing': 'Percentage of Missing Values'}
                    )
                )
            ]),
            dcc.Tab(label='bureau_balance', children=[
                dcc.Graph(
                    figure=px.line(
                        combined_df[combined_df['DataFrame'] == 'bureau_balance'],
                        x='Column Name',
                        y='Percentage Missing',
                        title='bureau_balance',
                        labels={'Percentage Missing': 'Percentage of Missing Values'}
                    )
                )
            ]),
            dcc.Tab(label='credit_card_balance', children=[
                dcc.Graph(
                    figure=px.line(
                        combined_df[combined_df['DataFrame'] == 'credit_card_balance'],
                        x='Column Name',
                        y='Percentage Missing',
                        title='credit_card_balance',
                        labels={'Percentage Missing': 'Percentage of Missing Values'}
                    )
                )
            ]),
            dcc.Tab(label='installments_payments', children=[
                dcc.Graph(
                    figure=px.line(
                        combined_df[combined_df['DataFrame'] == 'installments_payments'],
                        x='Column Name',
                        y='Percentage Missing',
                        title='installments_payments',
                        labels={'Percentage Missing': 'Percentage of Missing Values'}
                    )
                )
            ]),
            dcc.Tab(label='POS_CASH_balance', children=[
                dcc.Graph(
                    figure=px.line(
                        combined_df[combined_df['DataFrame'] == 'POS_CASH_balance'],
                        x='Column Name',
                        y='Percentage Missing',
                        title='POS_CASH_balance',
                        labels={'Percentage Missing': 'Percentage of Missing Values'}
                    )
                )
            ]),
        ])
    ], style={'padding': '20px'})
])

if __name__ == '__main__':
    app.run_server(debug=False)
