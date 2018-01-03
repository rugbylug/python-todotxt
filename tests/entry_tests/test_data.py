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
    (
        'x (A) 2017-01-03 2017-01-01 2017-01-03 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'x (A) 2017-01-01 2017-01-03 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        None
    ),
    (
        'x (A) 2017-01-01 2017-01-03 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'x (A) 2017-01-03 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        None
    ),
)

CREATED_DATE_TEST_TUPLE = (
    (
        '2017-01-01 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '2017-01-02 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '2017-01-02'
    ),
    (
        '2017-01-01 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        None
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
        '(A) 2017-01-01 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        '(A) Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        None
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
    (
        'Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        None
    ),
    (
        'x 2017-01-01 2017-01-01 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        'x 2017-01-01 Make @Cute +T1 +T2 c1:c2 c3:c4 with c-c-c-c-c',
        None
    ),
)


MERGE_TEST_TUPLE = (
    (
        'Make @Cute +T1 +T2 c1:c2 c3:c4 with',
        'Make @Cute2 +T1 +T2 c1:c2 c3:c4 with',
        'Make @Cute +T1 +T2 c1:c2 c3:c4 with @Cute2'
    ),
    (
        'Make @Cute +T1 +T2 c1:c2 c3:c4 with',
        'Make +T1 +T2 +T3 c1:c2 c3:c4 with',
        'Make @Cute +T1 +T2 c1:c2 c3:c4 with +T3'
    ),
    (
        'Make @Cute +T1 +T2 c1:c2 c3:c4 with',
        'Make +T1 +T2 +T3 c1:c2 c3:c4 with t5:t6',
        'Make @Cute +T1 +T2 c1:c2 c3:c4 with +T3 t5:t6'
    ),
    (
        'Make @Cute +T1 +T2 c1:c2 c3:c4 with t5:t6',
        'Make +T1 +T2 +T3 c1:c2 c3:c4 with t5:t6',
        'Make @Cute +T1 +T2 c1:c2 c3:c4 with t5:t6 +T3'
    ),
    (
        'x Make @Cute +T1 +T2 c1:c2 c3:c4 with t5:t6',
        'Make +T1 +T2 +T3 c1:c2 c3:c4 with t5:t6',
        'x Make @Cute +T1 +T2 c1:c2 c3:c4 with t5:t6 +T3'
    ),
    (
        'x 2017-01-04 2017-01-03 Make @Cute +T1 +T2 c1:c2 c3:c4 with t5:t6',
        'x 2017-01-05 2017-01-04 Make +T1 +T2 +T3 c1:c2 c3:c4 with t5:t6',
        'x 2017-01-05 2017-01-03 Make @Cute +T1 +T2 c1:c2 c3:c4 with t5:t6 +T3'
    ),
    (
        'Make @Cute +T1 +T2 c1:c2 c3:c4 with',
        'Make @Cute2 +T1 +T2 c1:c2 c3:c5 with',
        'Make @Cute +T1 +T2 c1:c2 c3:c4 with @Cute2 c3-merge0:c5'
    ),
    (
        'Make @Cute +T1 +T2 c1:c2 c3:c4 with @Cute2 c3-merge0:c5',
        'Make @Cute2 +T1 +T2 c1:c2 c3:c6 with',
        'Make @Cute +T1 +T2 c1:c2 c3:c4 with @Cute2 c3-merge0:c5 c3-merge1:c6'
    ),
)
