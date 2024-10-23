def queryHandler(provinces, jobs):
    queryHead = """SELECT employer, 
       SUM((requested_lmia + 0)) AS requested_lmia, 
       address,
       latitude, 
       longitude, 
       province, 
       LEFT(occupation, 4) AS occ 
       FROM lmia_tb 
"""
    queryTail = " GROUP BY employer,address, province, latitude, longitude, occ"
    queryConditions = []

    # Add conditions based on the provinces
    if provinces: 
        queryConditions.append("province IN (" + ', '.join(f"'{province}'" for province in provinces) + ")")
    
    # Add conditions based on the jobs
    if jobs: 
        queryConditions.append("occupation IN (" + ', '.join(f"'{job}'" for job in jobs) + ")")

    # Construct the final query
    if queryConditions:
        conditions_str = " AND ".join(queryConditions)
        return f"{queryHead} WHERE {conditions_str}{queryTail};"
    else:
        return f"{queryHead}{queryTail};"
