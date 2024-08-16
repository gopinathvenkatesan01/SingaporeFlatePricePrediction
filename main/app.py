import streamlit as st
import pickle
import numpy as np
import os


def main():
    page_icon_url = "https://github.com/user-attachments/assets/69df246e-ddca-4992-826a-e44889ddd698"
    st.set_page_config(
        page_title="Singapore Flat Price Prediction",
        page_icon=page_icon_url,
        layout="wide",
    )
    st.subheader("⏩ Singapore **Flat Price Prediction** | _By Gopi_ ")

    town_values = [
        "ANG MO KIO",
        "BEDOK",
        "BISHAN",
        "BUKIT BATOK",
        "BUKIT MERAH",
        "BUKIT TIMAH",
        "CENTRAL AREA",
        "CHOA CHU KANG",
        "CLEMENTI",
        "GEYLANG",
        "HOUGANG",
        "JURONG EAST",
        "JURONG WEST",
        "KALLANG/WHAMPOA",
        "MARINE PARADE",
        "QUEENSTOWN",
        "SENGKANG",
        "SERANGOON",
        "TAMPINES",
        "TOA PAYOH",
        "WOODLANDS",
        "YISHUN",
        "LIM CHU KANG",
        "SEMBAWANG",
        "BUKIT PANJANG",
        "PASIR RIS",
        "PUNGGOL",
    ]

    town_dict = {
        "SEMBAWANG": "NORTH",
        "SENGKANG": "NORTH",
        "WOODLANDS": "NORTH",
        "YISHUN": "NORTH",
        "BUKIT MERAH": "SOUTH",
        "BUKIT TIMAH": "SOUTH",
        "QUEENSTOWN": "SOUTH",
        "BEDOK": "EAST",
        "GEYLANG": "EAST",
        "HOUGANG": "EAST",
        "KALLANG/WHAMPOA": "EAST",
        "PASIR RIS": "EAST",
        "PUNGGOL": "EAST",
        "SERANGOON": "EAST",
        "TAMPINES": "EAST",
        "BUKIT BATOK": "WEST",
        "BUKIT PANJANG": "WEST",
        "CHOA CHU KANG": "WEST",
        "CLEMENTI": "WEST",
        "JURONG EAST": "WEST",
        "JURONG WEST": "WEST",
        "ANG MO KIO": "CENTRAL",
        "CENTRAL AREA": "CENTRAL",
        "BISHAN": "CENTRAL",
        "MARINE PARADE": "CENTRAL",
        "TOA PAYOH": "CENTRAL",
        "LIM CHU KANG": "NORTH",
    }

    town_region_dict = {"CENTRAL": 0, "EAST": 1, "WEST": 4, "SOUTH": 3, "NORTH": 2}

    flat_value = [
        "1 ROOM",
        "3 ROOM",
        "4 ROOM",
        "5 ROOM",
        "2 ROOM",
        "EXECUTIVE",
        "MULTI GENERATION",
    ]

    flat_dict = {
        "1 ROOM": 1,
        "2 ROOM": 2,
        "3 ROOM": 3,
        "4 ROOM": 4,
        "5 ROOM": 5,
        "EXECUTIVE": 6,
        "MULTI GENERATION": 7,
    }

    flat_model_value = [
        "IMPROVED",
        "NEW GENERATION",
        "MODEL A",
        "STANDARD",
        "SIMPLIFIED",
        "MODEL A-MAISONETTE",
        "APARTMENT",
        "MAISONETTE",
        "TERRACE",
        "2-ROOM",
        "IMPROVED-MAISONETTE",
        "MULTI GENERATION",
        "PREMIUM APARTMENT",
        "ADJOINED FLAT",
        "PREMIUM MAISONETTE",
        "MODEL A2",
        "DBSS",
        "TYPE S1",
        "TYPE S2",
        "PREMIUM APARTMENT LOFT",
        "3GEN",
    ]

    flat_model_dict = {
        "IMPROVED": 5,
        "NEW GENERATION": 12,
        "MODEL A": 8,
        "STANDARD": 17,
        "SIMPLIFIED": 16,
        "MODEL A-MAISONETTE": 9,
        "APARTMENT": 3,
        "MAISONETTE": 7,
        "TERRACE": 18,
        "2-ROOM": 0,
        "IMPROVED-MAISONETTE": 6,
        "MULTI GENERATION": 11,
        "PREMIUM APARTMENT": 13,
        "ADJOINED FLAT": 2,
        "PREMIUM MAISONETTE": 15,
        "MODEL A2": 10,
        "DBSS": 4,
        "TYPE S1": 19,
        "TYPE S2": 20,
        "PREMIUM APARTMENT LOFT": 14,
        "3GEN": 1,
    }

    lease_commence_value = [
        1966,
        1967,
        1968,
        1969,
        1970,
        1971,
        1972,
        1973,
        1974,
        1975,
        1976,
        1977,
        1978,
        1979,
        1980,
        1981,
        1982,
        1983,
        1984,
        1985,
        1986,
        1987,
        1988,
        1989,
        1990,
        1991,
        1992,
        1993,
        1994,
        1995,
        1996,
        1997,
        1998,
        1999,
        2000,
        2001,
        2002,
        2003,
        2004,
        2005,
        2006,
        2007,
        2008,
        2009,
        2010,
        2011,
        2012,
        2013,
        2014,
        2015,
        2016,
        2017,
        2018,
        2019,
        2020,
    ]

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    years = list(range(1990, 2025))

    # Custom CSS for the submit button
    st.markdown(
        """
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 80px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
        border: 2px solid #4CAF50;
    }
    .stButton button:hover {
        background-color: white;
        color: #4CAF50;
    }
    .prediction_win{
        font-size: 50px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-top: 20px;
    }
    .prediction_lost{
        font-size: 50px;
        font-weight: bold;
        color: #eb0707;
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    st.info("*Values Refered are based on given Data")
    with st.form("flat_price_predictor_form"):
        col1, col2, col3 = st.columns([0.5, 0.1, 0.5])

        with col1:

            selected_year = st.selectbox("Select Year", years)

            flat_type = st.selectbox(label="FlatType", options=flat_value)

            town = st.selectbox(label="Town", options=town_values)

            lease_commence_date = st.selectbox(
                label="Lease Commenced year", options=lease_commence_value
            )

            remaing_lease = st.number_input(
                label="*Remaing Lease Min 0", min_value=0.0, value=0.0
            )

        with col3:
            selected_month = st.selectbox("Select Month", months)

            month = months.index(selected_month) + 1

            flat_model = st.selectbox(label="FlatModel", options=flat_model_value)

            floor_area_sqm = st.number_input(
                label="*Floor Area Sqm Min 28 and Max 377",
                min_value=28.0,
                max_value=377.0,
                value=28.0,
            )

            storey_range = st.slider(
                "Storey Range", min_value=1, max_value=51, step=3, value=(3, 9)
            )

            st.write(" ")

            submitted = st.form_submit_button("Submit")

        if submitted:
            try:
                model_path = os.path.join(os.path.dirname(__file__), "models", "ml_flat_price_model_1_sqrt.pkl")
                with open(model_path, "rb") as f:
                    model = pickle.load(f)
                    town_region = town_dict[town]
                    town_part = town_region_dict[town_region]
                    start_storey, end_storey = storey_range
                    user_data = np.array(
                        [
                            [
                                month,
                                town_part,
                                flat_dict[flat_type],
                                floor_area_sqm,
                                flat_dict[flat_type],
                                lease_commence_date,
                                remaing_lease,
                                selected_year,
                                start_storey,
                                end_storey,
                            ]
                        ]
                    )

                    y_prediction = model.predict(user_data)
                    selling_price = y_prediction[0]

                    selling_price = round(selling_price, 2)

                    if selling_price > 0:
                        st.markdown(
                            f" <div class='prediction_win'>The Predicted Price is {selling_price}</div>",
                            unsafe_allow_html=True,
                        )

                    else:
                        st.markdown(
                            f"<div class='prediction_lost'>The Predicted Price is {selling_price}</div>",
                            unsafe_allow_html=True,
                        )

            except ValueError as e:
                st.warning("Please Provide Valid Remaing Lease/floor_area_sq")
            except Exception as e:
                st.warning(e)


if __name__ == "__main__":
    main()
