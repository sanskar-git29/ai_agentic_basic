from openai import OpenAI

client=OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
)

completion = client.chat.completions.create(
    model="qwen3.5:2b",
    messages=[
        {"role": "developer", "content": "Talk like a pirate."},
        {
            "role": "user",
            "content": "How do I check if a Python object is an instance of a class?",
        },
    ],
)

print(completion.choices[0].message.content)


# """

# ChatCompletion(id='chatcmpl-657', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='To check if a Python object is an instance of a specific class or its base classes, the recommended approach is using the built-in `isinstance()` function.\n\n### ✅ Recommended Method:`isinstance()`\n\n```python\nclass Animal:\n    pass\n\nclass Mammal(Animal):\n    pass\n\nclass Bird(Animal):\n    pass\n\nanimal = Animal()\nmammal = Mammal()\nbird = Bird()\n\n# Check instance of a class and base class\nprint(isinstance(animal, Animal))  # True\nprint(isinstance(mammal, Animal))  # True\nprint(isinstance(bird, Bird))      # True\n```\n\n### 📦 Other Approaches\n\nYou can also use `type()` to check the type hierarchy manually:\n\n```python\nclass MyClass:\n    pass\n\ninstance = MyClass()\n\n# Using type()\nprint(type(instance) == MyClass())  # Returns False (not a direct instance of its own class)\n\n# Or for baseclasses\nprint(isinstance(instance, type()))   # False - not helpful in this context\n```\n\n### 🔁 Checking for Multiple Classes or Subclasses\n\nFor checking multiple classes or all base classes:\n\n```python\nclass Cat:\n    def __init__(self):\n        print("Animal class")\n        self.age = 10\n\ndef check_types(obj, classes):\n    for cls in classes:\n        if isinstance(obj, cls):\n            print(f"✅ {obj.__class__.__name__} is an instance of {cls}")\n            return True\n    print(f"❌ {obj.__class__.__name__} is NOT an instance of any of the provided types")\n    return False\n\n# Example usage\ncheck_types(cat1,[Animal, Bird])  # Checks against multiple class instances\n```\n\n### 🚫 Avoiding Common Pitfalls\n\n- ✅Always prefer `isinstance()` for object-type checking.\n- ❌ Do not check if an instance of a class equalsa value directly using `==` or `type()` alone; they are not useful in most cases.\n\n### ⚙️ Quick ReferenceTable\n\n| Method       | Use Case                            | Example                        |\n|--------------|-------------------------------------|-------------------------------|\n| `isinstance()(|)` | Checkif an object is an instance of a class (or subclass)           | ✅ Best practice                  |\n| `type(obj)`     | Get the actual type of an object         | Useful for static analysis       |\n| `issubclass()`  | Check if a class is a subclass of another   | Not directly applicable in this context |\n\n### 📝 Example with `isinstance()` and Subclasses\n\n```python\nclass Person:\n    def __init__(self, name):\n  self.name = name\n\nclass Human(Person):\n    pass\n\nclass Animal:\n    pass\n\nperson = Person("John")\nhuman_instance = Human("Jane")\nanimal_instance = Animal()\n\nprint(isinstance(person, Person))  # True\nprint(isinstance(human_instance, Animal))  # False\nprint(isinstance(animal_instance, Animal))  # True\n```\n\n### ✅ Best Practice Recommendation\n\n> Use `isinstance()` for all object type checks to ensure clarity, maintainability, and compatibility. It is the most reliable method when working with classes in Python.', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None, reasoning="This is a straightforward question about Python object checking. The answer involves using the `isinstance()` function, which was introduced in Python 2 to simplify isinstance checks.\n\nLet me provide a clearexplanation with examples:\n\n1. **isinstance()** - This is the most common and recommended way to check if an object is an instance of a class or one of its base classes\n2. **Type** - Can use the `type()` function to get the type of an object, but it's not as useful as isinstance() for checking class relationships\n\nLet me give several examples with different scenarios."))], created=1795179165, model='qwen3.5:2b', object='chat.completion', metadata=None, moderation=None, service_tier=None, system_fingerprint='fp_ollama', usage=CompletionUsage(completion_tokens=825, prompt_tokens=25, total_tokens=850, completion_tokens_details=None, prompt_tokens_details=PromptTokensDetails(audio_tokens=None, cache_write_tokens=None, cached_tokens=0, image_tokens=None, text_tokens=None)))


# """




