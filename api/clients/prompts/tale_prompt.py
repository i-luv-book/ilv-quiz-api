class TalePromptGenerator:
  
  def processTaleFirstImagePrompt(self):
    return """
    # Instruction
    I'm going to make a picture for the fairy tale.
    It consists of three pages, and I will give you a one-line summary and background's description of a specific page, so make a picture that fits the page's information.

    # Tale Info
    1. Title: The Adventures of Jin and Sangik in the Enchanted Forest
    2. Characters’ Description
    - Jin: A brave boy with short black hair, wearing a green explorer’s outfit and carrying a lantern.
    - Sangik: A curious boy with curly brown hair, wearing a red shirt and blue overalls, holding a small backpack.
    3. Page's Information
    - Summary: Jin and Sangik discover a mysterious cave in the forest.
    - Background: Jin and Sangik discover a mysterious cave in the forest.
    """
    
talePromptGenerator = TalePromptGenerator()