# Power BI ESG Dashboard Schema

## Fact Table
**fact_carbon_emissions**
- product_id
- lifecycle_stage
- emissions_kgco2e
- cost_usd
- reporting_year

## Dimension Tables
- dim_product (product_name, revision, category)
- dim_supplier (supplier_name, esg_score, certified)
- dim_time (date, year, quarter, month)

## KPIs
- Total Carbon Footprint
- Scope-3 Contribution %
- Carbon Reduction %
- Cost vs Carbon Ratio
- Supplier ESG Risk Index
