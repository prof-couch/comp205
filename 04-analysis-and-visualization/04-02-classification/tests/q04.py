test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> testing_features.shape
          (20, 4)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(testing_features)
          <class 'numpy.ndarray'>
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
