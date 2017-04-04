# fb2rn

Rename FB2-files (eBooks) according to Autor and/or Title and/or Sequence
(pytnon3 and lxml)

    l or L - Lastname (without change) or LASTNAME 
    f or F - Firstname (without change) or FIRSTNAME
    t or T - Title (without change) or TITLE
    s or S - Sequencename (without change) or SEQUENCENAME
    n or N - Order in sequence (1,2,3,...)
    
    Example:
             python fb2rn.py +LFt book.fb2
             >> "AUTORLASTNAME AUTORFIRSTNAME Title.fb2"
             
             python fb2rn.py -LFt book.fb2
             >> "AUTORLASTNAMEAUTORFIRSTNAMETitle.fb2"
             
             python fb2rn.py -L_F_t book.fb2
             >> "AUTORLASTNAME_AUTORFIRSTNAME_Title.fb2"
