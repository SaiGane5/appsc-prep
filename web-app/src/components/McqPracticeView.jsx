import React, { useState } from 'react';
import MathText from './MathText';
import { 
  CheckCircle2, 
  XCircle, 
  HelpCircle, 
  Lightbulb, 
  RotateCcw, 
  Filter, 
  BookOpen
} from 'lucide-react';

export default function McqPracticeView({ mcqBank, allNotes, onSelectTopic }) {
  const [selectedSubject, setSelectedSubject] = useState('ALL');
  const [filterStatus, setFilterStatus] = useState('ALL'); // 'ALL', 'CORRECT', 'WRONG', 'UNATTEMPTED'
  const [userAnswers, setUserAnswers] = useState({});
  const [showExplanations, setShowExplanations] = useState({});

  // Parse raw text of MCQ into structured fields
  const parseQuestion = (rawText) => {
    try {
      const parts = rawText.split(/\(a\)|\(b\)|\(c\)|\(d\)|Correct Answer:/);
      const question = parts[0].trim();
      const optA = parts[1] ? parts[1].trim() : '';
      const optB = parts[2] ? parts[2].trim() : '';
      const optC = parts[3] ? parts[3].trim() : '';
      const rest = parts[4] ? parts[4].trim() : '';
      
      let optD = rest;
      let answerExplanation = '';
      if (rawText.includes('Correct Answer:')) {
        const idx = rawText.indexOf('Correct Answer:');
        answerExplanation = rawText.substring(idx).trim();
      }

      let correctKey = '';
      if (answerExplanation.includes('(a)')) correctKey = 'a';
      else if (answerExplanation.includes('(b)')) correctKey = 'b';
      else if (answerExplanation.includes('(c)')) correctKey = 'c';
      else if (answerExplanation.includes('(d)')) correctKey = 'd';

      let explanation = answerExplanation;
      const match = answerExplanation.match(/\[Explanation:\s*(.*?)\]/i);
      if (match) explanation = match[1];

      return {
        question,
        options: { a: optA, b: optB, c: optC, d: optD.split(/Correct Answer:/)[0].trim() },
        correctKey,
        explanation
      };
    } catch (e) {
      return null;
    }
  };

  const parsedBank = mcqBank.map((item, index) => ({
    id: `mcq-bank-${index}`,
    ...item,
    parsed: parseQuestion(item.raw_text)
  })).filter(item => item.parsed !== null);

  const subjects = ['ALL', ...new Set(parsedBank.map(q => q.subject_title))];

  // Filtering
  const filteredList = parsedBank.filter(q => {
    const matchesSubject = selectedSubject === 'ALL' || q.subject_title === selectedSubject;
    const answeredKey = userAnswers[q.id];
    let matchesStatus = true;
    if (filterStatus === 'CORRECT') {
      matchesStatus = answeredKey && answeredKey === q.parsed.correctKey;
    } else if (filterStatus === 'WRONG') {
      matchesStatus = answeredKey && answeredKey !== q.parsed.correctKey;
    } else if (filterStatus === 'UNATTEMPTED') {
      matchesStatus = !answeredKey;
    }
    return matchesSubject && matchesStatus;
  });

  // Calculate score statistics
  const totalAttempted = Object.keys(userAnswers).length;
  const totalCorrect = Object.entries(userAnswers).filter(([id, ans]) => {
    const q = parsedBank.find(item => item.id === id);
    return q && q.parsed.correctKey === ans;
  }).length;
  const accuracy = totalAttempted > 0 ? Math.round((totalCorrect / totalAttempted) * 100) : 0;

  const handleSelectOption = (qId, key) => {
    setUserAnswers(prev => ({ ...prev, [qId]: key }));
    setShowExplanations(prev => ({ ...prev, [qId]: true }));
  };

  const toggleExplanation = (qId) => {
    setShowExplanations(prev => ({ ...prev, [qId]: !prev[qId] }));
  };

  const handleResetQuiz = () => {
    if (window.confirm('Reset all your practice MCQ answers and score?')) {
      setUserAnswers({});
      setShowExplanations({});
    }
  };

  return (
    <div className="flex-1 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-5 mb-7 border-b border-[#303036]">
        <div>
          <h1 className="text-2xl sm:text-3xl font-bold text-white tracking-tight">
            Practice Objective Questions
          </h1>
          <p className="text-xs sm:text-sm text-zinc-400 mt-1">
            {parsedBank.length} Syllabus-mapped questions across all subjects with verified answers.
          </p>
        </div>

        {/* Minimal Scorecard */}
        <div className="flex items-center gap-3 bg-[#232327] border border-[#333338] p-2.5 rounded-lg shrink-0">
          <div className="text-center px-2">
            <div className="text-[10px] text-zinc-400 uppercase tracking-wide">Attempted</div>
            <div className="text-base font-semibold text-white font-mono">{totalAttempted}/{parsedBank.length}</div>
          </div>
          <div className="h-6 w-px bg-[#333338]"></div>
          <div className="text-center px-2">
            <div className="text-[10px] text-zinc-400 uppercase tracking-wide">Correct</div>
            <div className="text-base font-semibold text-white font-mono">{totalCorrect}</div>
          </div>
          <div className="h-6 w-px bg-[#333338]"></div>
          <div className="text-center px-2">
            <div className="text-[10px] text-zinc-400 uppercase tracking-wide">Accuracy</div>
            <div className="text-base font-semibold text-white font-mono">{accuracy}%</div>
          </div>
          <button
            onClick={handleResetQuiz}
            className="p-1.5 ml-1 text-zinc-400 hover:text-white hover:bg-[#2b2b30] rounded transition-colors"
            title="Reset Quiz"
          >
            <RotateCcw size={14} />
          </button>
        </div>
      </div>

      {/* Filters */}
      <div className="flex flex-wrap items-center justify-between gap-3 mb-6 bg-[#212125] p-2.5 rounded-lg border border-[#303036]">
        {/* Subject Filter */}
        <div className="flex items-center gap-2 overflow-x-auto max-w-full">
          <Filter size={13} className="text-zinc-400 shrink-0" />
          <span className="text-xs text-zinc-400 shrink-0">Subject:</span>
          <select
            value={selectedSubject}
            onChange={(e) => setSelectedSubject(e.target.value)}
            className="bg-[#18181b] border border-[#333338] text-xs text-white rounded px-2.5 py-1 focus:outline-none focus:border-zinc-400 max-w-xs"
          >
            {subjects.map((s, idx) => (
              <option key={idx} value={s}>
                {s === 'ALL' ? 'All Subjects' : s}
              </option>
            ))}
          </select>
        </div>

        {/* Status Filter */}
        <div className="flex items-center gap-1 text-xs">
          {['ALL', 'UNATTEMPTED', 'CORRECT', 'WRONG'].map(st => (
            <button
              key={st}
              onClick={() => setFilterStatus(st)}
              className={`px-2 py-0.5 rounded text-[11px] font-medium transition-colors ${
                filterStatus === st 
                  ? 'bg-zinc-200 text-zinc-900 font-semibold' 
                  : 'bg-[#28282d] text-zinc-400 hover:text-white hover:bg-[#323238]'
              }`}
            >
              {st}
            </button>
          ))}
        </div>
      </div>

      {/* Questions List */}
      <div className="space-y-5">
        {filteredList.map((item, qIdx) => {
          const qId = item.id;
          const { question, options, correctKey, explanation } = item.parsed;
          const selected = userAnswers[qId];
          const isRevealed = showExplanations[qId];
          const isCorrect = selected === correctKey;

          return (
            <div 
              key={qId}
              className="bg-[#222226] border border-[#303036] rounded-lg p-5 hover:border-[#404048] transition-colors"
            >
              {/* Question Meta */}
              <div className="flex flex-wrap items-center justify-between gap-2 mb-2.5">
                <span className="text-[11px] font-mono text-zinc-500 uppercase">
                  Q{qIdx + 1} • {item.topic_id}
                </span>
                <button
                  onClick={() => onSelectTopic(item.topic_id)}
                  className="text-xs text-zinc-400 hover:text-white flex items-center gap-1 transition-colors"
                >
                  <BookOpen size={11} />
                  <span>Topic: <MathText text={item.topic_title} /></span>
                </button>
              </div>

              {/* Question Text */}
              <h3 className="text-base font-medium text-white leading-snug mb-4">
                <MathText text={question} />
              </h3>

              {/* Options Grid */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-2 mb-3">
                {['a', 'b', 'c', 'd'].map(optKey => {
                  const optText = options[optKey];
                  if (!optText) return null;
                  const isThisSelected = selected === optKey;
                  const isThisCorrect = optKey === correctKey;

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
                      onClick={() => handleSelectOption(qId, optKey)}
                      className={btnClass}
                    >
                      <span className="font-mono font-semibold uppercase w-5 h-5 rounded bg-[#2a2a2f] flex items-center justify-center text-xs shrink-0 text-zinc-300">
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

              {/* Bottom Actions */}
              <div className="flex items-center justify-between pt-2.5 border-t border-[#2d2d33] text-xs">
                <button
                  onClick={() => toggleExplanation(qId)}
                  className="text-zinc-400 hover:text-white font-medium flex items-center gap-1.5 py-0.5 transition-colors"
                >
                  <HelpCircle size={13} />
                  {isRevealed ? 'Hide Explanation' : 'View Explanation'}
                </button>

                {selected && (
                  <span className="text-xs font-medium text-zinc-300">
                    {isCorrect ? '✓ Correct Choice' : `Option (${correctKey.toUpperCase()}) is correct`}
                  </span>
                )}
              </div>

              {/* Explanation Card */}
              {isRevealed && (
                <div className="mt-3 p-3.5 bg-[#1a1a1d] border border-[#333338] rounded text-xs leading-relaxed text-zinc-300">
                  <div className="font-semibold text-white mb-1 flex items-center gap-1.5">
                    <Lightbulb size={13} /> Correct Answer: Option ({correctKey.toUpperCase()})
                  </div>
                  <div>
                    <MathText text={explanation} />
                  </div>
                </div>
              )}
            </div>
          );
        })}

        {filteredList.length === 0 && (
          <div className="p-12 text-center text-zinc-500 bg-[#212125] rounded-lg border border-[#303036]">
            <p>No questions found matching your filter criteria.</p>
          </div>
        )}
      </div>
    </div>
  );
}
