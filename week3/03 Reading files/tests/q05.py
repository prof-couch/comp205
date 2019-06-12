test = {
  'name': 'Question 5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print(exer5)
          [(20. , 30. ,  4) (40.5, 50.5, 30) (60.2, 70.3, 50)]
          >>> isinstance(exer5[0][0], float) 
          True
          >>> isinstance(exer5[0][1], float)
          True
          >>> isinstance(exer5[0][2], np.int64) 
          True
          >>> print(exer5['carbon'])
          [20.  40.5 60.2]
          >>> print(exer5['nitrogen'])
          [30.  50.5 70.3]
          >>> print(exer5['oxygen'])
          [ 4 30 50]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
