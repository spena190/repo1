def handler(context, inputs):
    greeting = "Hello, {0}!".format(inputs["target"])
    print(greeting)
    
    print(" This is a test! ")

    outputs = {
      "greeting": greeting
    }

    return outputs
