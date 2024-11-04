import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group";
import appleLogo from "@/assets/apple.svg";
import nvidaLogo from "@/assets/nvidia.svg";
import toyotaLogo from "@/assets/toyota.svg";
import { AutosizeTextarea } from "@/components/ui/autosize-textarea";
import { TextGenerateEffect } from "@/components/ui/text-generate-effect";
import { useState } from "react";
import { Button } from "@/components/ui/button";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
} from "@/components/ui/select";

function App() {
  const [organization, setOrganization] = useState("apple");
  const [prompt, setPrompt] = useState("");
  const [answer, setAnswer] = useState("");
  const [model, setModel] = useState("gpt-3.5-turbo-instruct");

  const fetchAnswer = async () => {
    setAnswer("");
    const res = await fetch(`${import.meta.env.VITE_API_BASE_URL}/rag/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        organization,
        prompt,
        model,
      }),
    });
    const data = await res.text();
    setAnswer(data);
  };

  return (
    <div className="h-screen w-screen px-4 sm:px-10 bg-white mt-10">
      <ToggleGroup
        type="single"
        defaultValue="apple"
        value={organization}
        onValueChange={(value) => setOrganization(value)}
      >
        <ToggleGroupItem value="apple" aria-label="Toggle bold">
          <img src={appleLogo} alt="apple" className="h-6 w-6" />
        </ToggleGroupItem>
        <ToggleGroupItem value="nvidia" aria-label="Toggle italic">
          <img src={nvidaLogo} alt="nvidia" className="h-6 w-6" />
        </ToggleGroupItem>
        <ToggleGroupItem value="toyota" aria-label="Toggle underline">
          <img src={toyotaLogo} alt="toyota" className="h-6 w-6" />
        </ToggleGroupItem>
      </ToggleGroup>
      <div className="flex flex-col w-full gap-2">
        <div>
          <div className="text-gray-500 text-xl mb-3">Prompt</div>
          <AutosizeTextarea
            placeholder="Enter your prompt here..."
            className="max-w-[800px]"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
          />
          <Select value={model} onValueChange={(value) => setModel(value)}>
            <SelectTrigger value={model} className="max-w-[200px] mt-2">
              {model}
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="gpt-3.5-turbo-instruct">
                GPT-3.5 Turbo
              </SelectItem>
              <SelectItem value="babbage-002">Babbage 002</SelectItem>
              <SelectItem value="davinci-002">Davinci 002</SelectItem>
            </SelectContent>
          </Select>
          <Button className="mt-2" onClick={() => fetchAnswer()}>
            Get Answer
          </Button>
        </div>
        <div>
          <div className="text-gray-500 text-xl mb-3">Answer</div>
          {answer && <TextGenerateEffect words={answer} duration={1} />}
        </div>
      </div>
    </div>
  );
}

export default App;
