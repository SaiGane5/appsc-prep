import React, { useState } from 'react';
import MathText from './MathText';
import { 
  CheckCircle2, 
  XCircle, 
  HelpCircle, 
  ChevronDown, 
  ChevronUp, 
  BookOpen, 
  Lightbulb, 
  ZoomIn 
} from 'lucide-react';

export default function ContentRenderer({ content, onOpenImage, fontSizeMultiplier = 1 }) {
  const [selectedAnswers, setSelectedAnswers] = useState({});
  const [revealedExplanations, setRevealedExplanations] = useState({});
  const [expandedMains, setExpandedMains] = useState({});

  if (!Array.isArray(content)) return null;

  // Helper to parse MCQs from text
  const parseMcq = (text) => {
    const hasOptions = text.includes('(a)') && text.includes('(b)');
    const hasAnswer = text.includes('Correct Answer:');
    if (!hasOptions || !hasAnswer) return null;

    try {
      const parts = text.split(/\(a\)|\(b\)|\(c\)|\(d\)|Correct Answer:/);
      const questionText = parts[0].trim();
      const optA = parts[1] ? parts[1].trim() : '';
      const optB = parts[2] ? parts[2].trim() : '';
      const optC = parts[3] ? parts[3].trim() : '';
      const rest = parts[4] ? parts[4].trim() : '';
      
      let optD = rest;
      let answerExplanation = '';
      if (text.includes('Correct Answer:')) {
        const ansIndex = text.indexOf('Correct Answer:');
        answerExplanation = text.substring(ansIndex).trim();
      }

      let correctKey = '';
      if (answerExplanation.includes('(a)')) correctKey = 'a';
      else if (answerExplanation.includes('(b)')) correctKey = 'b';
      else if (answerExplanation.includes('(c)')) correctKey = 'c';
      else if (answerExplanation.includes('(d)')) correctKey = 'd';

      let explanation = '';
      const explMatch = answerExplanation.match(/\[Explanation:\s*(.*?)\]/i);
      if (explMatch) {
        explanation = explMatch[1];
      } else {
        explanation = answerExplanation;
      }

      return {
        questionText,
        options: {
          a: optA,
          b: optB,
          c: optC,
          d: optD.split(/Correct Answer:/)[0].trim()
        },
        correctKey,
        explanation
      };
    } catch (e) {
      return null;
    }
  };

  // Helper to parse Mains question
  const parseMains = (text) => {
    if (!text.includes('-> Model Approach:')) return null;
    const parts = text.split('-> Model Approach:');
    const question = parts[0].trim();
    const approach = parts[1] ? parts[1].trim() : '';
    return { question, approach };
  };

  const handleSelectOption = (qIndex, key) => {
    setSelectedAnswers(prev => ({ ...prev, [qIndex]: key }));
    setRevealedExplanations(prev => ({ ...prev, [qIndex]: true }));
  };

  const toggleExplanation = (qIndex) => {
    setRevealedExplanations(prev => ({ ...prev, [qIndex]: !prev[qIndex] }));
  };

  const toggleMains = (mIndex) => {
    setExpandedMains(prev => ({ ...prev, [mIndex]: !prev[mIndex] }));
  };

  const dynamicStyle = {
    fontSize: `${fontSizeMultiplier * 1}rem`
  };

  return (
    <div className="space-y-6 text-slate-200" style={dynamicStyle}>
      {content.map((item, idx) => {
        if (!item || !item.type) return null;

        // HEADING
        if (item.type === 'heading') {
          const headingId = `heading-${idx}-${encodeURIComponent(item.text.slice(0, 24).replace(/\s+/g, '-'))}`;
          if (item.level === 1) {
            return (
              <h1 
                key={idx} 
                id={headingId}
                className="text-2xl md:text-3xl font-bold text-white pt-6 pb-2 border-b border-[#2d2f3c] tracking-tight flex items-center gap-3"
              >
                <span className="w-1.5 h-8 bg-sky-400 rounded-full inline-block shrink-0"></span>
                <MathText text={item.text} />
              </h1>
            );
          } else if (item.level === 2) {
            return (
              <h2 
                key={idx} 
                id={headingId}
                className="text-xl md:text-2xl font-semibold text-slate-100 pt-5 pb-1 tracking-tight flex items-center gap-2"
              >
                <span className="w-1 h-5 bg-emerald-400 rounded-full inline-block shrink-0"></span>
                <MathText text={item.text} />
              </h2>
            );
          } else {
            return (
              <h3 
                key={idx} 
                id={headingId}
                className="text-lg md:text-xl font-medium text-amber-300 pt-3 pb-1"
              >
                <MathText text={item.text} />
              </h3>
            );
          }
        }

        // PARAGRAPH
        if (item.type === 'paragraph') {
          return (
            <p key={idx} className="text-slate-300 leading-relaxed text-[1.03rem] font-normal">
              <MathText text={item.text} />
            </p>
          );
        }

        // IMAGE
        if (item.type === 'image') {
          return (
            <div key={idx} className="image-card my-6">
              <div 
                className="relative group cursor-pointer overflow-hidden bg-black/40"
                onClick={() => onOpenImage && onOpenImage(item)}
              >
                <img 
                  src={item.url} 
                  alt={item.alt_text || 'Illustration'} 
                  loading="lazy"
                  className="w-full max-h-[440px] object-cover transition-transform duration-300 group-hover:scale-[1.01]"
                />
                <div className="absolute inset-0 bg-black/30 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
                  <span className="bg-black/75 text-white px-3.5 py-2 rounded-lg text-xs font-medium flex items-center gap-2 backdrop-blur-md">
                    <ZoomIn size={16} /> Click to View Full Resolution
                  </span>
                </div>
              </div>
              {item.caption && (
                <div className="image-caption flex items-start gap-2">
                  <span className="text-sky-400 font-semibold text-xs uppercase tracking-wide shrink-0 mt-0.5">Caption:</span>
                  <span><MathText text={item.caption} /></span>
                </div>
              )}
            </div>
          );
        }

        // TABLE
        if (item.type === 'table') {
          return (
            <div key={idx} className="table-container my-6">
              {item.caption && (
                <div className="table-caption">
                  <MathText text={item.caption} />
                </div>
              )}
              <table className="custom-table">
                <thead>
                  <tr>
                    {item.headers?.map((header, hIdx) => (
                      <th key={hIdx}>
                        <MathText text={header} />
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {item.rows?.map((row, rIdx) => (
                    <tr key={rIdx}>
                      {row.map((cell, cIdx) => (
                        <td key={cIdx}>
                          <MathText text={cell} />
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          );
        }

        // LIST
        if (item.type === 'list') {
          return (
            <div key={idx} className="my-4">
              {item.items?.map((listItem, lIdx) => {
                // Check if this item is an interactive MCQ
                const mcq = parseMcq(listItem);
                if (mcq) {
                  const qKey = `mcq-${idx}-${lIdx}`;
                  const selected = selectedAnswers[qKey];
                  const isRevealed = revealedExplanations[qKey];
                  const isCorrect = selected === mcq.correctKey;

                  return (
                    <div 
                      key={lIdx} 
                      className="bg-[#1b1c23] border border-[#2e303d] rounded-xl p-5 my-4 shadow-lg hover:border-[#3d4052] transition-colors"
                    >
                      <div className="flex items-start justify-between gap-3 mb-4">
                        <div className="font-semibold text-slate-100 text-base leading-snug">
                          <MathText text={mcq.questionText} />
                        </div>
                        <span className="badge badge-amber shrink-0 text-[11px]">
                          Prelims MCQ
                        </span>
                      </div>

                      <div className="grid grid-cols-1 md:grid-cols-2 gap-2.5 mb-3">
                        {['a', 'b', 'c', 'd'].map((optKey) => {
                          const optText = mcq.options[optKey];
                          if (!optText) return null;
                          const isThisSelected = selected === optKey;
                          const isThisCorrect = optKey === mcq.correctKey;
                          
                          let btnClass = "mcq-option-btn";
                          if (selected) {
                            if (isThisSelected) {
                              btnClass += isCorrect ? " selected-correct" : " selected-wrong";
                            } else if (isThisCorrect) {
                              btnClass += " show-actual-correct";
                            }
                          }

                          return (
                            <button
                              key={optKey}
                              onClick={() => handleSelectOption(qKey, optKey)}
                              className={btnClass}
                            >
                              <span className="font-mono font-bold uppercase w-6 h-6 rounded-md bg-[#252733] flex items-center justify-center text-xs shrink-0 text-slate-300">
                                {optKey}
                              </span>
                              <span className="flex-1 text-left">
                                <MathText text={optText} />
                              </span>
                              {selected && isThisCorrect && (
                                <CheckCircle2 size={18} className="text-emerald-400 shrink-0 mt-0.5" />
                              )}
                              {selected && isThisSelected && !isCorrect && (
                                <XCircle size={18} className="text-rose-400 shrink-0 mt-0.5" />
                              )}
                            </button>
                          );
                        })}
                      </div>

                      <div className="flex items-center justify-between pt-2 border-t border-[#2a2c38]">
                        <button
                          onClick={() => toggleExplanation(qKey)}
                          className="text-xs text-sky-400 hover:text-sky-300 font-medium flex items-center gap-1.5 py-1"
                        >
                          <HelpCircle size={14} />
                          {isRevealed ? 'Hide Explanation' : 'View Correct Answer & Explanation'}
                        </button>
                        {selected && (
                          <span className={`text-xs font-semibold ${isCorrect ? 'text-emerald-400' : 'text-rose-400'}`}>
                            {isCorrect ? '✓ Correct Choice!' : `✗ Incorrect (Correct is Option ${mcq.correctKey.toUpperCase()})`}
                          </span>
                        )}
                      </div>

                      {isRevealed && (
                        <div className="mt-3 p-3.5 bg-[#14151b] border border-[#2d303f] rounded-lg text-xs leading-relaxed text-slate-300 animate-fade-in">
                          <div className="font-bold text-emerald-400 mb-1 flex items-center gap-1.5">
                            <Lightbulb size={14} /> Correct Answer: Option ({mcq.correctKey.toUpperCase()})
                          </div>
                          <div>
                            <MathText text={mcq.explanation} />
                          </div>
                        </div>
                      )}
                    </div>
                  );
                }

                // Check if this item is a Mains Analytical question
                const mains = parseMains(listItem);
                if (mains) {
                  const mKey = `mains-${idx}-${lIdx}`;
                  const isExpanded = expandedMains[mKey];

                  return (
                    <div 
                      key={lIdx} 
                      className="bg-[#1b1c23] border border-[#2e303d] rounded-xl p-5 my-4 shadow-lg hover:border-[#3d4052] transition-colors"
                    >
                      <div className="flex items-start justify-between gap-3 mb-2">
                        <div className="font-semibold text-slate-100 text-base leading-snug">
                          <MathText text={mains.question} />
                        </div>
                        <span className="badge badge-cyan shrink-0 text-[11px]">
                          Mains (10M)
                        </span>
                      </div>

                      <button
                        onClick={() => toggleMains(mKey)}
                        className="w-full mt-3 p-2.5 bg-[#22242e] hover:bg-[#282a36] text-sky-400 rounded-lg text-xs font-medium flex items-center justify-between transition-colors"
                      >
                        <span className="flex items-center gap-2">
                          <BookOpen size={14} />
                          {isExpanded ? 'Collapse Model Answer Framework' : 'Expand Model Answer Approach & Structuring'}
                        </span>
                        {isExpanded ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                      </button>

                      {isExpanded && (
                        <div className="mt-3 p-4 bg-[#14151b] border border-sky-950/60 rounded-lg text-xs md:text-sm leading-relaxed text-slate-300 animate-fade-in">
                          <div className="font-bold text-sky-400 mb-1.5 flex items-center gap-1.5 uppercase tracking-wide">
                            <Lightbulb size={15} /> Evaluator's Blueprint / Model Approach:
                          </div>
                          <div className="whitespace-pre-line text-slate-200">
                            <MathText text={mains.approach} />
                          </div>
                        </div>
                      )}
                    </div>
                  );
                }

                // Regular List item
                return (
                  <div key={lIdx} className="flex items-start gap-3 my-2 text-slate-300 leading-relaxed">
                    <span className="w-2 h-2 rounded-full bg-sky-400 mt-2.5 shrink-0"></span>
                    <div className="flex-1">
                      <MathText text={listItem} />
                    </div>
                  </div>
                );
              })}
            </div>
          );
        }

        return null;
      })}
    </div>
  );
}
