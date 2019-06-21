test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> cluster.labels_.shape
          (150,)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(cluster.labels_)
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
