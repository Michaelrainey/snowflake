#!/usr/bin/env python
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL


donations = pd.read_csv('/Users/mrainey/Downloads/opendata_donations000.gz', escapechar='\\', names=['_donationid', '_projectid', '_donor_acctid', '_cartid', 'donor_city', 'donor_state', 'donor_zip', 'is_teacher_acct', 'donation_timestamp', 'donation_to_project', 'donation_optional_support', 'donation_total', 'donation_included_optional_support', 'payment_method', 'payment_included_acct_credit', 'payment_included_campaign_gift_card', 'payment_included_web_purchased_gift_card', 'payment_was_promo_matched', 'is_teacher_referred', 'giving_page_id', 'giving_page_type', 'for_honoree', 'thank_you_packet_mailed'])

resources = pd.read_csv('/Users/mrainey/Downloads/opendata_resources000.gz', escapechar='\\', names=['_resourceid', '_projectid', 'vendorid', 'vendor_name', 'item_name', 'item_number', 'item_unit_price', 'item_quantity'])

projects = pd.read_csv('/Users/mrainey/Downloads/opendata_projects000.gz', escapechar='\\', names=['_projectid', '_teacher_acctid', '_schoolid', 'school_ncesid', 'school_latitude', 'school_longitude', 'school_city', 'school_state', 'school_zip', 'school_metro', 'school_district', 'school_county', 'school_charter', 'school_magnet', 'school_year_round', 'school_nlns', 'school_kipp', 'school_charter_ready_promise', 'teacher_prefix', 'teacher_teach_for_america', 'teacher_ny_teaching_fellow', 'primary_focus_subject', 'primary_focus_area' ,'secondary_focus_subject', 'secondary_focus_area', 'resource_type', 'poverty_level', 'grade_level', 'vendor_shipping_charges', 'sales_tax', 'payment_processing_charges', 'fulfillment_labor_materials', 'total_price_excluding_optional_support', 'total_price_including_optional_support', 'students_reached', 'total_donations', 'num_donors', 'eligible_double_your_impact_match', 'eligible_almost_home_match', 'funding_status', 'date_posted', 'date_completed', 'date_thank_you_packet_mailed', 'date_expiration’])

engine = create_engine(URL(
    account = 'aws_cas2',
    user = 'mrainey',
    password = 'mySecretPassw0rd*',
    database = 'MRAINEY',
    schema = 'DONORSCHOOSE',
    warehouse = 'MRAINEYWH',
    role='DATA_LOADER',
))


try:
    conn = engine.connect()
    donations.to_sql('donations', con=conn, schema='DONORSCHOOSE', if_exists='replace', index=False, chunksize=10000)
    resources.to_sql('resources', con=conn, schema='DONORSCHOOSE', if_exists='replace', index=False, chunksize=10000)
    projects.to_sql('projects', con=conn, schema='DONORSCHOOSE', if_exists='replace', index=False, chunksize=10000)
finally:
    conn.close()
    engine.dispose()
