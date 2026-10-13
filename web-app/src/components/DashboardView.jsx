import React from 'react';
import { 
  CheckCircle2, 
  Star, 
  HelpCircle, 
  FileText, 
  ArrowRight
} from 'lucide-react';

export default function DashboardView({
  manifest,
  allNotes,
  completedTopics,
  bookmarks,
  onSelectTopic,
  onSwitchMode
}) {
  const totalTopics = allNotes.length;
  const completedCount = Object.values(completedTopics).filter(Boolean).length;
  const completionPercent = Math.round((completedCount / totalTopics) * 100);
  const bookmarkCount = Object.values(bookmarks).filter(Boolean).length;

  const totalWords = allNotes.reduce((acc, n) => acc + (n.word_count || 0), 0);

  // Bookmarked notes
  const bookmarkedNotes = allNotes.filter(n => bookmarks[n.topic_id]);

  return (
    <div className="flex-1 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Header */}
      <div className="pb-5 mb-7 border-b border-[#303036]">
        <h1 className="text-2xl sm:text-3xl font-bold text-white tracking-tight">
          Syllabus Progress & Overview
        </h1>
        <p className="text-xs sm:text-sm text-zinc-400 mt-1">
          Coverage tracking across all {manifest?.subjects?.length || 8} subjects and {totalTopics} topics.
        </p>
      </div>

      {/* Top Stat Cards Grid - Clean Monochrome */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-3.5 mb-7">
        <div className="bg-[#222226] border border-[#303036] p-4 rounded-lg">
          <div className="flex items-center justify-between text-zinc-400 text-xs mb-1.5">
            <span>Syllabus Covered</span>
            <CheckCircle2 size={14} className="text-zinc-400" />
          </div>
          <div className="text-2xl font-bold text-white font-mono">{completionPercent}%</div>
          <div className="text-[11px] text-zinc-500 mt-1">
            {completedCount} of {totalTopics} completed
          </div>
          <div className="w-full bg-[#18181b] h-1.5 rounded-full mt-2.5 overflow-hidden">
            <div 
              className="bg-zinc-300 h-full rounded-full transition-all duration-300" 
              style={{ width: `${completionPercent}%` }}
            />
          </div>
        </div>

        <div className="bg-[#222226] border border-[#303036] p-4 rounded-lg">
          <div className="flex items-center justify-between text-zinc-400 text-xs mb-1.5">
            <span>MCQ Practice</span>
            <HelpCircle size={14} className="text-zinc-400" />
          </div>
          <div className="text-2xl font-bold text-white font-mono">545</div>
          <div className="text-[11px] text-zinc-500 mt-1">
            Preliminary MCQs
          </div>
          <button
            onClick={() => onSwitchMode('mcqs')}
            className="text-[11px] text-zinc-300 hover:text-white font-medium flex items-center gap-1 mt-2.5"
          >
            Practice Questions <ArrowRight size={11} />
          </button>
        </div>

        <div className="bg-[#222226] border border-[#303036] p-4 rounded-lg">
          <div className="flex items-center justify-between text-zinc-400 text-xs mb-1.5">
            <span>Mains Repository</span>
            <FileText size={14} className="text-zinc-400" />
          </div>
          <div className="text-2xl font-bold text-white font-mono">134</div>
          <div className="text-[11px] text-zinc-500 mt-1">
            Analytical questions
          </div>
          <button
            onClick={() => onSwitchMode('mains')}
            className="text-[11px] text-zinc-300 hover:text-white font-medium flex items-center gap-1 mt-2.5"
          >
            Explore Questions <ArrowRight size={11} />
          </button>
        </div>

        <div className="bg-[#222226] border border-[#303036] p-4 rounded-lg">
          <div className="flex items-center justify-between text-zinc-400 text-xs mb-1.5">
            <span>Saved Topics</span>
            <Star size={14} className="text-zinc-400" />
          </div>
          <div className="text-2xl font-bold text-white font-mono">{bookmarkCount}</div>
          <div className="text-[11px] text-zinc-500 mt-1">
            Marked for quick review
          </div>
          <div className="text-[11px] text-zinc-500 mt-2.5 font-mono">
            ~{totalWords.toLocaleString()} words
          </div>
        </div>
      </div>

      {/* Subject-Wise Progress Breakdown */}
      <div className="bg-[#222226] border border-[#303036] rounded-lg p-5 mb-7">
        <h2 className="text-base font-semibold text-white mb-4">
          Subject Completion Breakdown
        </h2>

        <div className="space-y-3">
          {manifest?.subjects?.map(subject => {
            const subjectNotes = allNotes.filter(n => n.folder === subject.folder);
            const total = subjectNotes.length;
            const completed = subjectNotes.filter(n => completedTopics[n.topic_id]).length;
            const pct = total > 0 ? Math.round((completed / total) * 100) : 0;

            return (
              <div key={subject.folder} className="bg-[#1c1c1f] border border-[#2e2e34] p-3.5 rounded-md">
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-1.5 mb-2">
                  <div>
                    <h3 className="text-xs sm:text-sm font-medium text-white">
                      {subject.folder.replace(/^\d+_/, '').replace(/_/g, ' ')}
                    </h3>
                    <div className="text-[11px] text-zinc-400">{subject.paper}</div>
                  </div>
                  <div className="flex items-center gap-3 shrink-0">
                    <span className="text-xs font-mono text-zinc-400">
                      {completed}/{total} ({pct}%)
                    </span>
                    {subjectNotes.length > 0 && (
                      <button
                        onClick={() => {
                          onSelectTopic(subjectNotes[0].topic_id);
                          onSwitchMode('notes');
                        }}
                        className="px-2 py-0.5 text-xs bg-[#28282d] hover:bg-[#323238] text-zinc-300 hover:text-white rounded transition-colors"
                      >
                        Read
                      </button>
                    )}
                  </div>
                </div>

                <div className="w-full bg-[#141416] h-1.5 rounded-full overflow-hidden">
                  <div 
                    className="bg-zinc-400 h-full rounded-full transition-all duration-300"
                    style={{ width: `${pct}%` }}
                  />
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Bookmarked Topics Section */}
      {bookmarkedNotes.length > 0 && (
        <div className="bg-[#222226] border border-[#303036] rounded-lg p-5">
          <h2 className="text-base font-semibold text-white mb-3">
            Bookmarked Topics ({bookmarkedNotes.length})
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-2.5">
            {bookmarkedNotes.map(note => (
              <div
                key={note.topic_id}
                onClick={() => {
                  onSelectTopic(note.topic_id);
                  onSwitchMode('notes');
                }}
                className="p-3 bg-[#1c1c1f] border border-[#2e2e34] hover:border-zinc-500 rounded-md cursor-pointer transition-colors flex items-start justify-between gap-3 group"
              >
                <div className="min-w-0">
                  <div className="text-[10px] font-mono text-zinc-500 uppercase">{note.topic_id}</div>
                  <div className="text-xs font-medium text-white truncate group-hover:text-zinc-200">
                    {note.topic_title}
                  </div>
                  <div className="text-[11px] text-zinc-400 truncate mt-0.5">{note.subject_title}</div>
                </div>
                <ArrowRight size={13} className="text-zinc-500 group-hover:text-white shrink-0 mt-1 transition-colors" />
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
