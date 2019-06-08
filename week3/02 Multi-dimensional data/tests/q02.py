test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> clean_columns(np.array([[1,2,3],[4,5,6],[7,8,9]]))
          array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
          >>> clean_columns(np.array([[1,2,3],[4,-1,6],[7,8,9]]))
          array([[1, 3],
                 [4, 6],
                 [7, 9]])
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
