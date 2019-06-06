test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> (renorm(np.array([1,2,3])) == np.array([-1.,0.,1.])).all() 
          True
          >>> (renorm(np.array([5,6,7,8,9])) == np.array([-2.,-1.,0.,1.,2.])).all()
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
