'''
ideas :
-  recursive blocks           [by default]
- (order left hand side ?)    [by default]
- dependency across blocks
- dummy blocks that are basically substituted everywhere else
'''

# import os, yaml

# this_dir, this_filename = os.path.split(__file__)
# DATA_PATH = os.path.join(this_dir, "recipes.yaml")

# with file(DATA_PATH) as f:
#   recipes = yaml.load(f)
import yaml
recipes = yaml.load('''fg:

    model_type: fg

    variable_type: ['states', 'controls']

    equation_type:

        arbitrage:
            - ['states',0]
            - ['controls',0]
            - ['states',1]
            - ['controls',1]

        transition:

            definition: True

            lhs:
                - ['states',0]

            rhs:
                - ['states',-1]
                - ['controls',-1]
                - ['shocks',0]
fg2:

    model_type: fg2

    variable_type: ['states', 'controls']

    equation_type:

        arbitrage:
            - ['states',0]
            - ['controls',0]
            - ['shocks',1]
            - ['states',1]
            - ['controls',1]

        transition:

            definition: True

            lhs:
                - ['states',0]

            rhs:
                - ['states',-1]
                - ['controls',-1]
                - ['shocks',0]



fga:

  model_type: fga

  variable_type: ['states', 'controls', 'auxiliary']

  equation_type:

      arbitrage:
          - ['states',0]
          - ['controls',0]
          - ['auxiliary',0]
          - ['states',1]
          - ['controls',1]
          - ['auxiliary',1]

      transition:

          definition: True

          lhs:
              - ['states',0]

          rhs:
              - ['states',-1]
              - ['controls',-1]
              - ['auxiliary',-1]
              - ['shocks',0]

      auxiliary:

          definition: True

          lhs:
              - ['auxiliary',0]

          rhs:
              - ['states',0]
              - ['controls',0]

fgh1:

  model_type: fgh1

  variable_type: ['states', 'controls', 'expectations']

  equation_type:

      arbitrage:
          - ['states',0]
          - ['controls',0]
          - ['expectations',0]


      transition:

          definition: True

          lhs:
              - ['states',0]

          rhs:
              - ['states',-1]
              - ['controls',-1]
              - ['shocks',0]

      expectation:

          definition: True

          lhs:
              - ['expectations',0]

          rhs:
              - ['states',1]
              - ['controls',1]

fgh2:

  model_type: fgh2

  variable_type: ['states', 'controls', 'expectations']

  equation_type:

      arbitrage:
          - ['states',0]
          - ['controls',0]
          - ['expectations',0]


      transition:

          definition: True

          lhs:
              - ['states',0]

          rhs:
              - ['states',-1]
              - ['controls',-1]
              - ['shocks',0]

      expectation:

          definition: True

          lhs:
              - ['expectations',0]

          rhs:
              - ['states',0]
              - ['controls',0]
              - ['shocks',1]
              - ['states',1]
              - ['controls',1]



vfi:

  model_type: vfi

  variable_type: ['states', 'controls', 'utility']

  equation_type:

      utility:

          definition: True

          lhs:
              - ['utility',0]

          rhs:
              - ['states',0]
              - ['controls',0]

      transition:

          definition: True

          lhs:
              - ['states',0]

          rhs:
              - ['states',-1]
              - ['controls',-1]
              - ['shocks',0]


''')
