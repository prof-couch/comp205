test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> training_features.shape
          (130, 4)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(training_features)
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
