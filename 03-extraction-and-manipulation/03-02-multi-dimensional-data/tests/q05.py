test = {
  'name': 'Question 5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print(default_missing(np.array([[1,2,3],[4,5,6],[7,8,9]]))) 
          [[1. 2. 3.]
           [4. 5. 6.]
           [7. 8. 9.]]
          >>> print(default_missing(np.array([[1,2,3],[1,2,-1],[1,2,3]])))   
          [[1. 2. 3.]
           [1. 2. 3.]
           [1. 2. 3.]]
          >>> print(default_missing(np.array([[1,-1,3],[1,2,-1],[-1,2,3]])))             
          [[1. 2. 3.]
           [1. 2. 3.]
           [1. 2. 3.]]
          >>> print(default_missing(np.array([[2,4,6],[4,-1,8],[-1,8,-1]])))             
          [[2. 4. 6.]
           [4. 6. 8.]
           [3. 8. 7.]]
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
