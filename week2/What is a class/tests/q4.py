test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(purchases) # doctest:+NORMALIZE_WHITESPACE
          <class '__main__.Purchases'>
          >>> type(purchases.purchases)
          <class 'list'>
          >>> print(purchases.purchases[0]) # doctest:+NORMALIZE_WHITESPACE
          The cost of socks is 10.0
          >>> print(purchases.purchases[1]) # doctest:+NORMALIZE_WHITESPACE
          The cost of tie is 20.0
          >>> print(purchases.purchases[2]) # doctest:+NORMALIZE_WHITESPACE
          The cost of shoes is 50.0
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
