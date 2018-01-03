PRIORITY_TEST_TUPLE = (
    (
        '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '(B) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'B'
    ),
    (
        'x (A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'x (B) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'B'
    ),
    (
        'x (A) xxxx Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'x (B) xxxx Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'B'
    ),
    (
        'Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '(B) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'B'
    ),
    (
        'x Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'x (B) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'B'
    ),
    (
        '(A) (A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '(B) (A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'B'
    ),
    (
        '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        None
    ),
    (
        'x (A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'x Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        None
    )
)


COMPLETED_TEST_TUPLE = (
    (
        'x (A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'x (A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        True
    ),
    (
        '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'x (A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        True
    ),
    (
        'x (A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        False
    ),
    (
        '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        False
    ),
    (
        'x(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'x(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        False
    ),
    (
        'x(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'x x(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        True
    )
)


COMPLETED_DATE_TEST_TUPLE = (
    (
        'x (A) 2017-01-01 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'x (A) 2017-01-02 2017-01-01 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '2017-01-02'
    ),
    (
        'x (A) 2017-01-03 2017-01-01 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'x (A) 2017-01-02 2017-01-01 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '2017-01-02'
    ),
    (
        'x (A) 2017-01-03 2017-01-01 2017-01-03 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'x (A) 2017-01-02 2017-01-01 2017-01-03 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '2017-01-02'
    ),
)

CREATED_DATE_TEST_TUPLE = (
    (
        '2017-01-01 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '2017-01-02 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '2017-01-02'
    ),
    (
        'Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '2017-01-02 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '2017-01-02'
    ),
    (
        'x Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'x 2017-01-02 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '2017-01-02'
    ),
    (
        '(A) 2017-01-01 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '(A) 2017-01-02 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '2017-01-02'
    ),
    (
        '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '(A) 2017-01-02 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '2017-01-02'
    ),
    (
        'x (A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'x (A) 2017-01-02 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '2017-01-02'
    ),
    (
        'x 2017-01-01 2017-01-01 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'x 2017-01-01 2017-01-02 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '2017-01-02'
    ),
)
