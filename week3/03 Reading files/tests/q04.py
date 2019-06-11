test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print(exer4)
          [(20. , 30. ,  4) (40.5, 50.5, 30) (60.2, 70.3, 50)]
          >>> isinstance(exer4[0][0], float) 
          True
          >>> isinstance(exer4[0][1], float)
          True
          >>> isinstance(exer4[0][2], np.int64) 
          True
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
