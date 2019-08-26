test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print(column_averages(np.array([[1,1,1],[1,1,1],[1,1,1]])))
          [1. 1. 1.]
          >>> print(column_averages(np.array([[1,2,3],[1,2,3],[1,2,3]])))
          [1. 2. 3.]
          >>> print(column_averages(np.array([[1,2,3],[5,6,7]])))
          [3. 4. 5.]
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
