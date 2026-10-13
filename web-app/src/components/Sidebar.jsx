import React, { useState } from 'react';
import { 
  CheckCircle, 
  Circle, 
  ChevronRight, 
  ChevronDown, 
  Search, 
  X, 
  Star
} from 'lucide-react';

export default function Sidebar({
  manifest,
  allNotes,
  activeTopicId,
  onSelectTopic,
  completedTopics,
  onToggleComplete,
  bookmarks,
  onToggleBookmark,
  isOpen,
  onClose,
  searchQuery,
  setSearchQuery,
  paperFilter,
  setPaperFilter
}) {
  const [openSubjects, setOpenSubjects] = useState(() => {
    const init = {};
    manifest?.subjects?.forEach(s => { init[s.folder] = true; });
    return init;
  });

  const toggleSubject = (folder) => {
    setOpenSubjects(prev => ({ ...prev, [folder]: !prev[folder] }));
  };

  const filteredNotes = allNotes.filter(note => {
    const matchesSearch = !searchQuery || 
      note.topic_title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      note.syllabus_mapping.toLowerCase().includes(searchQuery.toLowerCase()) ||
      note.subject_title.toLowerCase().includes(searchQuery.toLowerCase());

    const matchesPaper = !paperFilter || paperFilter === 'ALL' ||
      (note.paper && note.paper.toLowerCase().includes(paperFilter.toLowerCase()));

    return matchesSearch && matchesPaper;
  });

  const papers = [
    { id: 'ALL', label: 'All' },
    { id: 'Paper-II', label: 'Paper II' },
    { id: 'Paper-III', label: 'Paper III' },
    { id: 'Paper-IV', label: 'Paper IV' },
    { id: 'Paper-V', label: 'Paper V' },
    { id: 'Screening', label: 'Screening' }
  ];

  return (
    <>
      {/* Mobile backdrop */}
      {isOpen && (
        <div 
          className="fixed inset-0 bg-black/80 z-40 lg:hidden backdrop-blur-sm transition-opacity"
          onClick={onClose}
        />
      )}

      {/* Sidebar Container */}
      <aside className={`
        fixed inset-y-0 left-0 z-40 w-80 bg-[#16171d] border-r border-[#2d2f3c] flex flex-col transition-transform duration-300 ease-in-out
        lg:static lg:h-full lg:shrink-0 lg:translate-x-0
        ${isOpen ? 'translate-x-0 shadow-2xl' : '-translate-x-full'}
      `}>
        {/* Header */}
        <div className="p-3.5 border-b border-[#2d2f3c] bg-[#1a1b22] shrink-0">
          <div className="flex items-center justify-between mb-2.5">
            <div className="flex items-center gap-2">
              <div className="w-7 h-7 rounded-lg bg-sky-500/20 border border-sky-500/40 flex items-center justify-center text-sky-400 font-bold text-xs">
                AP
              </div>
              <div>
                <h2 className="text-xs font-bold text-white tracking-tight">Syllabus Index</h2>
                <div className="text-[10px] text-slate-400">40 Comprehensive Topics</div>
              </div>
            </div>
            <button 
              onClick={onClose}
              className="lg:hidden p-1 text-slate-400 hover:text-white rounded-lg hover:bg-slate-800"
            >
              <X size={18} />
            </button>
          </div>

          {/* Search Box */}
          <div className="relative mb-2">
            <Search size={14} className="absolute left-2.5 top-1/2 -translate-y-1/2 text-slate-400" />
            <input 
              type="text"
              placeholder="Filter topics..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-8 pr-7 py-1.5 bg-[#121318] border border-[#2e303e] rounded-lg text-xs text-white placeholder-slate-500 focus:outline-none focus:border-sky-400 transition-colors"
            />
            {searchQuery && (
              <button 
                onClick={() => setSearchQuery('')}
                className="absolute right-2 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white"
              >
                <X size={12} />
              </button>
            )}
          </div>

          {/* Paper Filter Pills */}
          <div className="flex items-center gap-1 overflow-x-auto pb-0.5 no-scrollbar text-[10px]">
            {papers.map(p => (
              <button
                key={p.id}
                onClick={() => setPaperFilter(p.id)}
                className={`px-2 py-0.5 rounded-md shrink-0 transition-colors font-medium ${
                  paperFilter === p.id 
                    ? 'bg-sky-500 text-white shadow-sm' 
                    : 'bg-[#22242e] text-slate-400 hover:text-white hover:bg-[#2b2d3a]'
                }`}
              >
                {p.label}
              </button>
            ))}
          </div>
        </div>

        {/* Subjects & Topics Tree */}
        <div className="flex-1 overflow-y-auto p-2.5 space-y-2.5">
          {manifest?.subjects?.map((subject) => {
            const subjectNotes = filteredNotes.filter(n => n.folder === subject.folder);
            if (subjectNotes.length === 0 && (searchQuery || paperFilter !== 'ALL')) {
              return null;
            }

            const totalInSubject = subject.topics.length;
            const completedInSubject = subject.topics.filter(t => {
              const matchedNote = allNotes.find(n => n.folder === subject.folder && n.file_name === t.file);
              return matchedNote && completedTopics[matchedNote.topic_id];
            }).length;

            const isExpanded = openSubjects[subject.folder] ?? true;

            return (
              <div key={subject.folder} className="bg-[#1b1c24] border border-[#2b2d39] rounded-xl overflow-hidden shadow-sm">
                <button
                  onClick={() => toggleSubject(subject.folder)}
                  className="w-full px-3 py-2.5 flex items-center justify-between text-left hover:bg-[#22242e] transition-colors"
                >
                  <div className="flex items-center gap-2 min-w-0 pr-1">
                    <span className="text-slate-400">
                      {isExpanded ? <ChevronDown size={14} /> : <ChevronRight size={14} />}
                    </span>
                    <span className="text-xs font-semibold text-white truncate">
                      {subject.folder.replace(/^\d+_/, '').replace(/_/g, ' ')}
                    </span>
                  </div>
                  <span className="text-[10px] font-mono text-slate-400 px-1.5 py-0.5 rounded bg-[#121318] border border-[#2e303d] shrink-0">
                    {completedInSubject}/{totalInSubject}
                  </span>
                </button>

                {isExpanded && (
                  <div className="p-1 space-y-0.5 border-t border-[#262833] bg-[#16171f]">
                    {subject.topics.map((topicItem) => {
                      const note = allNotes.find(n => n.folder === subject.folder && n.file_name === topicItem.file);
                      if (!note) return null;
                      
                      const isVisible = filteredNotes.some(fn => fn.topic_id === note.topic_id);
                      if (!isVisible) return null;

                      const isActive = note.topic_id === activeTopicId;
                      const isCompleted = !!completedTopics[note.topic_id];
                      const isBookmarked = !!bookmarks[note.topic_id];

                      return (
                        <div
                          key={note.topic_id}
                          className={`
                            group flex items-center justify-between px-2.5 py-1.5 rounded-lg text-xs cursor-pointer transition-all
                            ${isActive 
                              ? 'bg-sky-500/15 border border-sky-500/35 text-white font-medium shadow-sm' 
                              : 'text-slate-300 hover:bg-[#22242e] hover:text-white border border-transparent'}
                          `}
                          onClick={() => {
                            onSelectTopic(note.topic_id);
                            if (window.innerWidth < 1024) onClose();
                          }}
                        >
                          <div className="flex items-start gap-2 min-w-0 pr-1">
                            <button
                              onClick={(e) => {
                                e.stopPropagation();
                                onToggleComplete(note.topic_id);
                              }}
                              className="mt-0.5 text-slate-500 hover:text-emerald-400 transition-colors shrink-0"
                              title={isCompleted ? 'Mark Incomplete' : 'Mark Completed'}
                            >
                              {isCompleted ? (
                                <CheckCircle size={13} className="text-emerald-400 fill-emerald-400/20" />
                              ) : (
                                <Circle size={13} />
                              )}
                            </button>
                            <span className="truncate leading-snug">
                              {note.topic_title}
                            </span>
                          </div>

                          <div className="flex items-center gap-1 shrink-0 ml-1">
                            <button
                              onClick={(e) => {
                                e.stopPropagation();
                                onToggleBookmark(note.topic_id);
                              }}
                              className={`p-0.5 rounded transition-colors ${
                                isBookmarked 
                                  ? 'text-amber-400 hover:text-amber-300' 
                                  : 'text-slate-600 hover:text-slate-400 opacity-0 group-hover:opacity-100'
                              }`}
                              title={isBookmarked ? 'Remove Bookmark' : 'Bookmark Topic'}
                            >
                              <Star size={12} fill={isBookmarked ? 'currentColor' : 'none'} />
                            </button>
                          </div>
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </aside>
    </>
  );
}
