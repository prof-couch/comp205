test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print(masked(np.array([[1,2,3],[4,5,6],[7,8,9]])))
          [[1 2 3]
           [4 5 6]
           [7 8 9]]
          >>> print(masked(np.array([[1,2,3],[4,-1,6],[7,8,9]])))
          [[1 2 3]
           [4 -- 6]
           [7 8 9]]
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
