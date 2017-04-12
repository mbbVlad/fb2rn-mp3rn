# fb2rn

Rename FB2-files (eBooks) according to Autor and/or Title and/or Sequence
(pytnon3 and lxml, was tested: Win8 and Linux Mint)

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

# Music files (mp3, ...)

Rename Music-files according to Artist and/or Title and/or Track
(pytnon3 and mutagen, was tested: Win8 and Linux Mint on mp3-files)

    a or A - Artist (without change) or ARTIST 
    t or T - Title (without change) or TITLE
    r or R - Track
    y or Y - Year
    g or G - Genre (without change) or GENRE
    b or B - Album (without change) or ALBUM
    Example:
             python mp3rn.py +At mus.mp3
             >> "ARTIST Title.mp3"

            python mp3rn.py -At mus.mp3
             >> "ARTISTTitle.mp3"
             
            python mp3rn.py -A_t mus.mp3
             >> "ARTIST_Title.mp3"
