import Greenly_CaseStudy.streamlit as st
import datetime
import pandas as pd
import numpy as np
import altair as alt

head = st.container()
dashboard = st.container()

with head: 
    centered_text1 = """
    <div style="text-align: center;">
        <h3>The Good, The Bad, and the Unsubscribed</h1>
        <p>A Dashboard for Email Campaign KPIs</p>
    </div>
    """

    # Display centered Markdown text
    st.markdown(centered_text1, unsafe_allow_html=True)

with dashboard: 
    with st.sidebar:
        date_from = st.date_input('From', datetime.date(2022, 5, 1))
        date_to = st.date_input('To', datetime.date(2022, 6, 1))
        d = date_to - date_from
        st.write(f'Total Duration: {d.days} days')
        if st.button('Today'): 
            date_to = datetime.date(2023, 5, 29)
        camp_id = st.multiselect('Campaign ID', [106, 16, 47, 64, 67, 68, 69, 77, 202])
        email_ids = st.multiselect('Email ID/Action ID', [61, 62, 986, 1073, 996, 197])
        country = st.selectbox(
        'Contact Country',
        ('France', 'UK', 'USA'))

    tab1, tab2, tab3 = st.tabs(['Overview and Comparison','A/B Test Analysis', 'Conversion Over Time'])
    with tab1: 
        centered_text2 = """
        <div style="text-align: center;">
            <h5>Overview</h5>
        </div>
        """
        st.markdown(centered_text2, unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric(label="Total # of emails sent", value="10395", delta="18")
        col1.metric(label="Average Deliverability rate", value="95%", delta="0.1%")
        col2.metric(label="Average Bounce Rate", value="1.5%", delta="-0.2%")
        col2.metric(label="Average Open Rate", value="24%", delta="1.4%")
        col3.metric(label="Average Click Rate", value="4%", delta="0.5%")
        col3.metric(label="Average Reactivity", value="10%", delta="-0.2%")
        col4.metric(label="Average Ubsubscribe Rate", value="0.4%", delta="-0.1%")
        col4.metric(label="Average Conversion Rate", value="5%", delta="-0.1%")

        st.write('')
        st.write('')

        centered_text2 = """
        <div style="text-align: center;">
            <h5>Campaign Comparison</h5>
            <p>Select one or more campaign ID in the left side filter. </p>
            <p>(Also, in this part, I want to add a horizontal line in each graph indicating the average of the metric. )</p>
        </div>
        """
        st.markdown(centered_text2, unsafe_allow_html=True)

        col5, col6 = st.columns(2)
        
        num_sent_email_bar = pd.DataFrame({
            'Number of Sent Emails': np.random.randint(100, 500, size=(len(camp_id), 1)).flatten(),
            'camp_id': camp_id,
        })
        num_sent_chart = alt.Chart(num_sent_email_bar).mark_bar().encode(
            x='camp_id:O',  # 'O' indicates that this is an ordinal scale
            y='Number of Sent Emails:Q',  # 'Q' indicates that this is a quantitative scale
            color='camp_id:N'  # 'N' indicates nominal scale. Here, color is determined by the 'camp_id' column
        )
        col5.write(num_sent_chart)

        deliverability_rate_bar = pd.DataFrame({
            'Deliverability Rate': np.random.randint(85, 99, size=(len(camp_id), 1)).flatten(),
            'camp_id': camp_id,
        })
        deliverability_chart = alt.Chart(deliverability_rate_bar).mark_bar().encode(
            x='camp_id:O',  # 'O' indicates that this is an ordinal scale
            y='Deliverability Rate:Q',  # 'Q' indicates that this is a quantitative scale
            color='camp_id:N'  # 'N' indicates nominal scale. Here, color is determined by the 'camp_id' column
        )
        col5.write(deliverability_chart)

        bounce_rate_bar = pd.DataFrame({
            'Bounce Rate': np.round(np.random.uniform(0.5, 2.5, size=(len(camp_id), 1)),2).flatten(),
            'camp_id': camp_id,
        })
        bounce_rate_chart = alt.Chart(bounce_rate_bar).mark_bar().encode(
            x='camp_id:O',
            y='Bounce Rate:Q',
            color='camp_id:N'
        )
        col6.write(bounce_rate_chart)

        open_rate_bar = pd.DataFrame({
            'Open Rate': np.random.randint(20, 30, size=(len(camp_id), 1)).flatten(),
            'camp_id': camp_id,
        })
        open_rate_chart = alt.Chart(open_rate_bar).mark_bar().encode(
            x='camp_id:O',
            y='Open Rate:Q',
            color='camp_id:N'
        )
        col5.write(open_rate_chart)

        click_rate_bar = pd.DataFrame({
            'Click Rate': np.round(np.random.uniform(3, 9, size=(len(camp_id), 1)), 2).flatten(),
            'camp_id': camp_id,
        })
        click_rate_chart = alt.Chart(click_rate_bar).mark_bar().encode(
            x='camp_id:O',
            y='Click Rate:Q',
            color='camp_id:N'
        )
        col6.write(click_rate_chart)

        reactivity_bar = pd.DataFrame({
            'Reactivity': np.round(np.random.uniform(5, 15, size=(len(camp_id), 1)), 2).flatten(),
            'camp_id': camp_id,
        })
        reactivity_chart = alt.Chart(reactivity_bar).mark_bar().encode(
            x='camp_id:O',
            y='Reactivity:Q',
            color='camp_id:N'
        )
        col5.write(reactivity_chart)

        unsubscribe_rate_bar = pd.DataFrame({
            'Unsubscribe Rate': np.round(np.random.uniform(0.1, 0.9, size=(len(camp_id), 1)), 2).flatten(),
            'camp_id': camp_id,
        })
        unsubscribe_rate_chart = alt.Chart(unsubscribe_rate_bar).mark_bar().encode(
            x='camp_id:O',
            y='Unsubscribe Rate:Q',
            color='camp_id:N'
        )
        col6.write(unsubscribe_rate_chart)

        conversion_rate_bar = pd.DataFrame({
            'Conversion Rate': np.round(np.random.uniform(5, 10, size=(len(camp_id), 1)), 2).flatten(),
            'camp_id': camp_id,
        })
        conversion_rate_chart = alt.Chart(conversion_rate_bar).mark_bar().encode(
            x='camp_id:O',
            y='Conversion Rate:Q',
            color='camp_id:N'
        )
        col6.write(conversion_rate_chart)


    with tab2: 
        centered_text4 = """
        <div style="text-align: center;">
            <h5>A/B test for action_id in the same campaign</h5>
            <p>Select one or more action ID (of the same campaign ID) in the left side filter. </p>
        </div>
        """
        st.markdown(centered_text4, unsafe_allow_html=True)

        st.write('')

        col9, col10 = st.columns(2)
        kpi = col9.selectbox(
            'Select a KPI to compute the p-value for the 2 action_id performance',
            ('Deliverability', 'Bounce', 'Open', 'Click', 'Unsubscribe'))
        confidence = col10.radio(
            "Select a confidence level",
            ('90%', '95%', '99%'))
        if len(email_ids)>1: 
            st.warning(f'There\'s a significant difference in {kpi} rates between action_id {email_ids[0]} and {email_ids[1]}.')
        st.write('')
        st.write('')
        st.write('')

        col7, col8 = st.columns(2)

        num_sent_email_bar = pd.DataFrame({
            'Number of Sent Emails': np.random.randint(100, 500, size=(len(email_ids), 1)).flatten(),
            'email_ids': email_ids,
        })
        num_sent_chart = alt.Chart(num_sent_email_bar).mark_bar().encode(
            x='email_ids:O',  # 'O' indicates that this is an ordinal scale
            y='Number of Sent Emails:Q',  # 'Q' indicates that this is a quantitative scale
            color='email_ids:N'  # 'N' indicates nominal scale. Here, color is determined by the 'email_ids' column
        )
        col7.write(num_sent_chart)

        deliverability_rate_bar = pd.DataFrame({
            'Deliverability Rate': np.random.randint(85, 99, size=(len(email_ids), 1)).flatten(),
            'email_ids': email_ids,
        })
        deliverability_chart = alt.Chart(deliverability_rate_bar).mark_bar().encode(
            x='email_ids:O',  # 'O' indicates that this is an ordinal scale
            y='Deliverability Rate:Q',  # 'Q' indicates that this is a quantitative scale
            color='email_ids:N'  # 'N' indicates nominal scale. Here, color is determined by the 'email_ids' column
        )
        col7.write(deliverability_chart)

        bounce_rate_bar = pd.DataFrame({
            'Bounce Rate': np.round(np.random.uniform(0.5, 2.5, size=(len(email_ids), 1)), 2).flatten(),
            'email_ids': email_ids,
        })
        bounce_rate_chart = alt.Chart(bounce_rate_bar).mark_bar().encode(
            x='email_ids:O',
            y='Bounce Rate:Q',
            color='email_ids:N'
        )
        col8.write(bounce_rate_chart)

        open_rate_bar = pd.DataFrame({
            'Open Rate': np.random.randint(20, 30, size=(len(email_ids), 1)).flatten(),
            'email_ids': email_ids,
        })
        open_rate_chart = alt.Chart(open_rate_bar).mark_bar().encode(
            x='email_ids:O',
            y='Open Rate:Q',
            color='email_ids:N'
        )
        col7.write(open_rate_chart)

        click_rate_bar = pd.DataFrame({
            'Click Rate': np.round(np.random.uniform(3, 9, size=(len(email_ids), 1)), 2).flatten(),
            'email_ids': email_ids,
        })
        click_rate_chart = alt.Chart(click_rate_bar).mark_bar().encode(
            x='email_ids:O',
            y='Click Rate:Q',
            color='email_ids:N'
        )
        col8.write(click_rate_chart)

        reactivity_bar = pd.DataFrame({
            'Reactivity': np.round(np.random.uniform(5, 15, size=(len(email_ids), 1)), 2).flatten(),
            'email_ids': email_ids,
        })
        reactivity_chart = alt.Chart(reactivity_bar).mark_bar().encode(
            x='email_ids:O',
            y='Reactivity:Q',
            color='email_ids:N'
        )
        col7.write(reactivity_chart)

        unsubscribe_rate_bar = pd.DataFrame({
            'Unsubscribe Rate': np.round(np.random.uniform(0.1, 0.9, size=(len(email_ids), 1)), 2).flatten(),
            'email_ids': email_ids,
        })
        unsubscribe_rate_chart = alt.Chart(unsubscribe_rate_bar).mark_bar().encode(
            x='email_ids:O',
            y='Unsubscribe Rate:Q',
            color='email_ids:N'
        )
        col8.write(unsubscribe_rate_chart)

        conversion_rate_bar = pd.DataFrame({
            'Conversion Rate': np.round(np.random.uniform(5, 10, size=(len(email_ids), 1)), 2).flatten(),
            'email_ids': email_ids,
        })
        conversion_rate_chart = alt.Chart(conversion_rate_bar).mark_bar().encode(
            x='email_ids:O',
            y='Conversion Rate:Q',
            color='email_ids:N'
        )
        col8.write(conversion_rate_chart)

    with tab3: 
        centered_text3 = """
        <div style="text-align: center;">
            <h5>Conversion at a campaign level over time</h5>
            <p>Select one or more campaign ID in the left side filter. </p>
        </div>
        """
        st.markdown(centered_text3, unsafe_allow_html=True)
        # trend_line_nb_sent = pd.DataFrame(np.random.randint(100, 1000, (d.days,1)), columns=[f'Campaign ID {camp_id}'])
        # st.line_chart(trend_line_nb_sent)
        data = []
        for camp in camp_id:
            dates = pd.date_range(date_from, date_to)
            conversion_rate = np.round(np.random.uniform(5, 10, size=(len(dates), 1)), 2)
            for date, rate in zip(dates, conversion_rate):
                data.append({'date': date, 'campaign': camp, 'conversion_rate': rate[0]})

        df = pd.DataFrame(data)

        # Create the line chart with Altair
        chart = alt.Chart(df).mark_line().encode(
            x='date:T',
            y='conversion_rate:Q',
            color='campaign:N',
            tooltip=['date:T', 'campaign:N', 'conversion_rate:Q']
        )

        st.altair_chart(chart, use_container_width=True)