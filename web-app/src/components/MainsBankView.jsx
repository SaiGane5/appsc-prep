import React, { useState } from 'react';
import MathText from './MathText';
import { 
  BookOpen, 
  ChevronDown, 
  ChevronUp, 
  Lightbulb, 
  Search, 
  Filter, 
  FileText, 
  Award,
  Layers
} from 'lucide-react';

export default function MainsBankView({ mainsBank, onSelectTopic }) {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedSubject, setSelectedSubject] = useState('ALL');
  const [expandedItems, setExpandedItems] = useState({});

  // Parse questions
  const parseMainsItem = (rawText) => {
    if (!rawText.includes('-> Model Approach:')) {
      return { question: rawText, approach: '' };
    }
    const parts = rawText.split('-> Model Approach:');
    return {
      question: parts[0].trim(),
      approach: parts[1] ? parts[1].trim() : ''
    };
  };

  const parsedList = mainsBank.map((item, idx) => ({
    id: `mains-${idx}`,
    ...item,
    parsed: parseMainsItem(item.raw_text)
  }));

  const subjects = ['ALL', ...new Set(parsedList.map(q => q.subject_title))];

  const filteredList = parsedList.filter(item => {
    const matchesSubject = selectedSubject === 'ALL' || item.subject_title === selectedSubject;
    const matchesSearch = !searchQuery || 
      item.parsed.question.toLowerCase().includes(searchQuery.toLowerCase()) ||
      item.parsed.approach.toLowerCase().includes(searchQuery.toLowerCase()) ||
      item.topic_title.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesSubject && matchesSearch;
  });

  const toggleExpand = (id) => {
    setExpandedItems(prev => ({ ...prev, [id]: !prev[id] }));
  };

  const expandAll = () => {
    const all = {};
    filteredList.forEach(item => { all[item.id] = true; });
    setExpandedItems(all);
  };

  const collapseAll = () => {
    setExpandedItems({});
  };

  return (
    <div className="flex-1 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 animate-fade-in">
      {/* Header */}
      <div className="pb-6 mb-8 border-b border-[#2d2f3c]">
        <span className="badge badge-cyan mb-2">Mains Examination Repository</span>
        <h1 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
          APPSC Group-1 Mains Analytical Question Bank
        </h1>
        <p className="text-xs sm:text-sm text-slate-400 mt-1">
          141 descriptive and analytical questions spanning Paper-II, Paper-III, Paper-IV, and Paper-V, equipped with structural model approaches, mark distributions, and evaluator blueprints.
        </p>
      </div>

      {/* Search and Filters */}
      <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 mb-6 bg-[#181920] p-3 rounded-xl border border-[#2b2d39]">
        <div className="relative flex-1">
          <Search size={14} className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
          <input
            type="text"
            placeholder="Search questions or keywords..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-9 pr-3 py-1.5 bg-[#20222d] border border-[#2e3140] rounded-lg text-xs text-white placeholder-slate-500 focus:outline-none focus:border-sky-400"
          />
        </div>

        <div className="flex items-center gap-2">
          <select
            value={selectedSubject}
            onChange={(e) => setSelectedSubject(e.target.value)}
            className="bg-[#20222d] border border-[#2e3140] text-xs text-white rounded-lg px-2.5 py-1.5 focus:outline-none focus:border-sky-400"
          >
            {subjects.map((s, idx) => (
              <option key={idx} value={s}>
                {s === 'ALL' ? 'All Subjects' : s}
              </option>
            ))}
          </select>

          <button
            onClick={expandAll}
            className="px-2.5 py-1.5 bg-[#242633] hover:bg-[#2c2f3f] text-slate-300 text-xs font-medium rounded-lg transition-colors shrink-0"
          >
            Expand All
          </button>
          <button
            onClick={collapseAll}
            className="px-2.5 py-1.5 bg-[#242633] hover:bg-[#2c2f3f] text-slate-300 text-xs font-medium rounded-lg transition-colors shrink-0"
          >
            Collapse All
          </button>
        </div>
      </div>

      {/* Question Counter */}
      <div className="text-xs text-slate-400 mb-4 flex items-center justify-between">
        <span>Showing {filteredList.length} of {parsedList.length} Mains Questions</span>
      </div>

      {/* List of Questions */}
      <div className="space-y-4">
        {filteredList.map((item, index) => {
          const isExpanded = !!expandedItems[item.id];
          const { question, approach } = item.parsed;

          return (
            <div
              key={item.id}
              className="bg-[#1b1c24] border border-[#2d2f3c] rounded-xl p-5 shadow-md hover:border-[#3d4052] transition-colors"
            >
              <div className="flex flex-wrap items-center justify-between gap-2 mb-2.5">
                <div className="flex items-center gap-2">
                  <span className="text-[11px] font-mono text-sky-400 font-semibold">
                    #{index + 1} • {item.topic_id}
                  </span>
                  <span className="badge badge-cyan text-[10px]">
                    10 Marks
                  </span>
                </div>
                <button
                  onClick={() => onSelectTopic(item.topic_id)}
                  className="text-xs text-slate-400 hover:text-sky-300 flex items-center gap-1 transition-colors"
                >
                  <BookOpen size={12} />
                  <span>Topic: <MathText text={item.topic_title} /></span>
                </button>
              </div>

              <h3 className="text-base sm:text-lg font-semibold text-white leading-snug mb-3">
                <MathText text={question} />
              </h3>

              {approach && (
                <div>
                  <button
                    onClick={() => toggleExpand(item.id)}
                    className="w-full mt-1 p-2.5 bg-[#22242e] hover:bg-[#282a36] text-sky-400 rounded-lg text-xs font-medium flex items-center justify-between transition-colors"
                  >
                    <span className="flex items-center gap-2">
                      <Lightbulb size={14} />
                      {isExpanded ? 'Hide Model Answer Approach' : 'View Model Answer Approach & Structural Blueprint'}
                    </span>
                    {isExpanded ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                  </button>

                  {isExpanded && (
                    <div className="mt-3 p-4 bg-[#14151b] border border-sky-950/60 rounded-lg text-xs sm:text-sm leading-relaxed text-slate-300 animate-fade-in">
                      <div className="font-bold text-sky-400 mb-1.5 flex items-center gap-1.5 uppercase tracking-wide text-xs">
                        <Award size={14} /> Answer Structuring Strategy:
                      </div>
                      <div className="whitespace-pre-line text-slate-200">
                        <MathText text={approach} />
                      </div>
                    </div>
                  )}
                </div>
              )}
            </div>
          );
        })}

        {filteredList.length === 0 && (
          <div className="p-12 text-center text-slate-500 bg-[#16171f] rounded-xl border border-[#2b2d39]">
            <p>No Mains questions found matching your filter criteria.</p>
          </div>
        )}
      </div>
    </div>
  );
}
