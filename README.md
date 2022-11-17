1. GET : localhost:7003/api/v1/status
    
    - returns {"success": true}

2. GET : localhost:7003/api/v1/sentences/page
      - page is the input integer to return 10 sentences in a list of dictionary.

      - If the page number is greater than (length of dataframe * 10)-1 the response is "THERE ARE ONLY : 100 TRANSLATIONS PLEASE ENTER PAGE NUMBER FROM 0 to 9 ONLY"
