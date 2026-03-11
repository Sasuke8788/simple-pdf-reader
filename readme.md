# PDF Q&A App

This project is a terminal-based chatbot that answers questions from a PDF document using LangChain, ChromaDB, and Google Gemini.

## Domain

**Chosen Domain:** AI / Machine Learning (Transformers)

The chatbot is configured to read `data/transformers.pdf`, so questions and answers are focused on transformer models, attention, architecture, and related ML concepts.

## Setup Instructions

1. Clone the repository and open it in VS Code.
2. Create and activate a virtual environment.
3. Install dependencies.
4. Add your Google API key to a `.env` file.
5. Run the app.

### Commands (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

Run the chatbot:

```powershell
python app.py
```

Type your question at the prompt. Type `exit` or `quit` to stop.

## Example Questions and Chatbot Answers

1. **Question:** What is this PDF about?
	**Answer:** This PDF is about a research paper titled "Attention Is All You Need." It introduces a new simple network architecture called the **Transformer**, which is based solely on **attention mechanisms** and dispenses with recurrent and convolutional neural networks.

	The paper discusses its application to sequence transduction models, specifically mentioning experiments with an English-to-German base translation model, and illustrates how attention heads function, for example, in anaphora resolution.

2. **Question:** Why is the name "Attention Is All You Need"?
	**Answer:** The title "Attention Is All You Need" reflects the core contribution of the paper, which is the introduction of the Transformer model.

	The Transformer is a new network architecture that **relies solely on attention mechanisms**, specifically self-attention, and **dispenses with recurrence and convolutions**. The paper demonstrates that attention alone is sufficient to achieve state-of-the-art performance in sequence transduction tasks, suggesting that other complex components (like recurrent or convolutional neural networks) are not "needed."

3. **Question:** What does a transformer do?
	**Answer:** The Transformer is a sequence transduction model that uses an encoder-decoder structure. Its primary function is to:

	1. **Encoder:** Map an input sequence of symbol representations to a sequence of continuous representations.
	2. **Decoder:** Generate an output sequence of symbols one element at a time, consuming previously generated symbols as additional input.

	It achieves this by relying entirely on an attention mechanism (specifically self-attention) to draw global dependencies between its input and output, without using sequence-aligned recurrent neural networks (RNNs) or convolutions.
