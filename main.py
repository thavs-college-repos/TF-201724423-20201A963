import numpy as np
import pandas as pd
import plotly.express as px
from src.data import calles, intersc


def main() -> None:
    f = open('.mapbox_token', "w+")
    f.write('pk.eyJ1IjoidTIwMTcyNDQyMyIsImEiOiJjbDN2eHZpaDgwMHdrM2txcHd5YzlwempxIn0.iDkPaJgRqFMJjiBW8_gVEQ')
    f.close()

    px.set_mapbox_access_token(open(".mapbox_token").read())

    df = intersc()
    df['factor_trafico'] = np.random.randint(1, 4, df.shape[0])
    query_df = df.query("calles_name in ['Plaza 2 de Mayo', '9 de Octubre']")
    graph_df = query_df

    fig = px.line_mapbox(graph_df, lat="start_lat", lon="start_log", line_group="calle_id",
                         hover_name='calle_name', zoom=12)
    fig.show()


if __name__ == "__main__":
    main()
