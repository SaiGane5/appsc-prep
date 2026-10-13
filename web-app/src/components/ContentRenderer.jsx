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
    fontSize: `${fontSizeMultiplier * 1.0625}rem`
  };

  return (
    <div className="space-y-6 text-zinc-300" style={dynamicStyle}>
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
                className="text-2xl sm:text-3xl font-bold text-white pt-8 pb-3 border-b border-[#303036] tracking-tight leading-snug"
              >
                <MathText text={item.text} />
              </h1>
            );
          } else if (item.level === 2) {
            return (
              <h2 
                key={idx} 
                id={headingId}
                className="text-xl sm:text-2xl font-semibold text-zinc-100 pt-7 pb-2 tracking-tight leading-snug"
              >
                <MathText text={item.text} />
              </h2>
            );
          } else {
            return (
              <h3 
                key={idx} 
                id={headingId}
                className="text-lg font-semibold text-zinc-200 pt-5 pb-1 leading-snug"
              >
                <MathText text={item.text} />
              </h3>
            );
          }
        }

        // PARAGRAPH
        if (item.type === 'paragraph') {
          return (
            <p key={idx} className="text-[#d4d4d8] leading-[1.8] font-normal my-4">
              <MathText text={item.text} />
            </p>
          );
        }

        // IMAGE
        if (item.type === 'image') {
          return (
            <div key={idx} className="image-card my-6">
              <div 
                className="relative group cursor-pointer overflow-hidden bg-black/30"
                onClick={() => onOpenImage && onOpenImage(item)}
              >
                <img 
                  src={item.url} 
                  alt={item.alt_text || 'Illustration'} 
                  loading="lazy"
                  className="w-full max-h-[440px] object-cover transition-opacity duration-200 group-hover:opacity-95"
                />
                <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
                  <span className="bg-[#1e1e22]/90 text-white px-3 py-1.5 rounded-md text-xs font-medium flex items-center gap-1.5 border border-[#38383e]">
                    <ZoomIn size={14} /> Full Resolution
                  </span>
                </div>
              </div>
              {item.caption && (
                <div className="image-caption text-zinc-400">
                  <MathText text={item.caption} />
                </div>
              )}
            </div>
          );
        }

        // TABLE
        if (item.type === 'table') {
          return (
            <div key={idx} className="my-6 rounded-lg border border-[#333338] bg-[#222226] overflow-hidden">
              {item.caption && (
                <div className="table-title-bar">
                  <MathText text={item.caption} />
                </div>
              )}
              <div className="overflow-x-auto w-full">
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
                      className="bg-[#232327] border border-[#333338] rounded-lg p-5 my-4 hover:border-[#44444c] transition-colors"
                    >
                      <div className="font-medium text-white text-base leading-snug mb-4">
                        <MathText text={mcq.questionText} />
                      </div>

                      <div className="grid grid-cols-1 md:grid-cols-2 gap-2 mb-3">
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
                              <span className="font-mono font-semibold uppercase w-5 h-5 rounded bg-[#2b2b30] flex items-center justify-center text-xs shrink-0 text-zinc-300">
                                {optKey}
                              </span>
                              <span className="flex-1 text-left text-sm leading-snug">
                                <MathText text={optText} />
                              </span>
                              {selected && isThisCorrect && (
                                <CheckCircle2 size={16} className="text-zinc-300 shrink-0 mt-0.5" />
                              )}
                              {selected && isThisSelected && !isCorrect && (
                                <XCircle size={16} className="text-zinc-400 shrink-0 mt-0.5" />
                              )}
                            </button>
                          );
                        })}
                      </div>

                      <div className="flex items-center justify-between pt-2.5 border-t border-[#2e2e34]">
                        <button
                          onClick={() => toggleExplanation(qKey)}
                          className="text-xs text-zinc-400 hover:text-white font-medium flex items-center gap-1.5 py-0.5 transition-colors"
                        >
                          <HelpCircle size={13} />
                          {isRevealed ? 'Hide Explanation' : 'View Explanation'}
                        </button>
                        {selected && (
                          <span className="text-xs font-medium text-zinc-300">
                            {isCorrect ? '✓ Correct' : `Option (${mcq.correctKey.toUpperCase()}) is correct`}
                          </span>
                        )}
                      </div>

                      {isRevealed && (
                        <div className="mt-3 p-3.5 bg-[#1a1a1d] border border-[#333338] rounded text-xs leading-relaxed text-zinc-300">
                          <div className="font-semibold text-white mb-1 flex items-center gap-1.5">
                            <Lightbulb size={13} /> Answer: Option ({mcq.correctKey.toUpperCase()})
                          </div>
                          <div className="text-zinc-300">
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
                      className="bg-[#232327] border border-[#333338] rounded-lg p-5 my-4 hover:border-[#44444c] transition-colors"
                    >
                      <div className="font-medium text-white text-base leading-snug mb-3">
                        <MathText text={mains.question} />
                      </div>

                      <button
                        onClick={() => toggleMains(mKey)}
                        className="w-full mt-2 p-2 bg-[#2a2a2f] hover:bg-[#323238] text-zinc-300 rounded text-xs font-medium flex items-center justify-between transition-colors"
                      >
                        <span className="flex items-center gap-1.5">
                          <BookOpen size={13} />
                          {isExpanded ? 'Hide Model Approach' : 'Model Answer Approach & Structure'}
                        </span>
                        {isExpanded ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
                      </button>

                      {isExpanded && (
                        <div className="mt-3 p-3.5 bg-[#1a1a1d] border border-[#333338] rounded text-xs sm:text-sm leading-relaxed text-zinc-300">
                          <div className="font-semibold text-white mb-1.5 text-xs uppercase tracking-wide">
                            Model Approach:
                          </div>
                          <div className="whitespace-pre-line text-zinc-300">
                            <MathText text={mains.approach} />
                          </div>
                        </div>
                      )}
                    </div>
                  );
                }

                // Regular List item
                return (
                  <div key={lIdx} className="flex items-start gap-2.5 my-2.5 text-[#d4d4d8] leading-[1.75]">
                    <span className="w-1.5 h-1.5 rounded-full bg-zinc-400 mt-2.5 shrink-0"></span>
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
