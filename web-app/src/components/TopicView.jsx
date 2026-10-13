import React, { useState } from 'react';
import ContentRenderer from './ContentRenderer';
import MathText from './MathText';
import { 
  CheckCircle, 
  Circle, 
  Star, 
  Clock, 
  FileText, 
  Printer, 
  ArrowLeft, 
  ArrowRight, 
  ChevronDown, 
  ChevronUp, 
  BookMarked,
  Share2,
  Bookmark
} from 'lucide-react';

export default function TopicView({
  note,
  allNotes,
  onSelectTopic,
  isCompleted,
  onToggleComplete,
  isBookmarked,
  onToggleBookmark,
  onOpenImage,
  fontSizeMultiplier
}) {
  const [syllabusExpanded, setSyllabusExpanded] = useState(false);

  if (!note) {
    return (
      <div className="flex-1 flex items-center justify-center p-12 text-slate-500">
        <p>Select a topic from the syllabus index to begin reading.</p>
      </div>
    );
  }

  // Find previous and next topics
  const currentIndex = allNotes.findIndex(n => n.topic_id === note.topic_id);
  const prevTopic = currentIndex > 0 ? allNotes[currentIndex - 1] : null;
  const nextTopic = currentIndex < allNotes.length - 1 ? allNotes[currentIndex + 1] : null;

  // Extract headings for quick table of contents
  const headings = note.content
    ?.filter(item => item.type === 'heading')
    ?.map((h, i) => ({
      text: h.text,
      level: h.level,
      id: `heading-${i}-${encodeURIComponent(h.text.slice(0, 24).replace(/\s+/g, '-'))}`
    })) || [];

  const handlePrint = () => {
    window.print();
  };

  return (
    <article className="flex-1 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8 animate-fade-in">
      {/* Top Meta Bar */}
      <div className="flex flex-wrap items-center justify-between gap-3 pb-4 mb-6 border-b border-[#2d2f3c] text-xs">
        <div className="flex flex-wrap items-center gap-2">
          <span className="badge badge-indigo">
            {note.subject_title}
          </span>
          <span className="badge badge-cyan">
            {note.paper}
          </span>
          <span className="text-slate-400 flex items-center gap-1">
            <Clock size={13} /> {note.estimated_read_time_mins} min read
          </span>
          <span className="text-slate-500 hidden sm:inline">
            • {note.word_count?.toLocaleString()} words
          </span>
        </div>

        {/* Action Controls */}
        <div className="flex items-center gap-2">
          <button
            onClick={() => onToggleBookmark(note.topic_id)}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg border text-xs font-medium transition-colors ${
              isBookmarked 
                ? 'bg-amber-500/15 border-amber-500/40 text-amber-300' 
                : 'bg-[#1e202a] border-[#313342] text-slate-300 hover:text-white hover:bg-[#262835]'
            }`}
          >
            <Star size={13} fill={isBookmarked ? 'currentColor' : 'none'} />
            <span className="hidden sm:inline">{isBookmarked ? 'Bookmarked' : 'Bookmark'}</span>
          </button>

          <button
            onClick={() => onToggleComplete(note.topic_id)}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg border text-xs font-medium transition-colors ${
              isCompleted 
                ? 'bg-emerald-500/15 border-emerald-500/40 text-emerald-300' 
                : 'bg-[#1e202a] border-[#313342] text-slate-300 hover:text-white hover:bg-[#262835]'
            }`}
          >
            {isCompleted ? <CheckCircle size={13} /> : <Circle size={13} />}
            <span className="hidden sm:inline">{isCompleted ? 'Completed' : 'Mark Done'}</span>
          </button>

          <button
            onClick={handlePrint}
            className="p-1.5 text-slate-400 hover:text-white rounded-lg bg-[#1e202a] border border-[#313342] hover:bg-[#262835] transition-colors"
            title="Print or Save PDF"
          >
            <Printer size={15} />
          </button>
        </div>
      </div>

      {/* Main Title */}
      <header className="mb-6">
        <div className="text-xs font-mono font-semibold text-sky-400 tracking-wider uppercase mb-1">
          {note.topic_id}
        </div>
        <h1 className="text-2xl sm:text-3xl md:text-4xl font-extrabold text-white tracking-tight leading-tight">
          <MathText text={note.topic_title} />
        </h1>
      </header>

      {/* Syllabus Mapping Card */}
      {note.syllabus_mapping && (
        <div className="mb-8 bg-[#181a22] border border-[#2b2d39] rounded-xl overflow-hidden shadow-sm">
          <button
            onClick={() => setSyllabusExpanded(!syllabusExpanded)}
            className="w-full px-4 py-3 bg-[#20222d] flex items-center justify-between text-left text-xs font-semibold text-slate-200 hover:text-white transition-colors"
          >
            <span className="flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-sky-400"></span>
              Official APPSC Syllabus Mapping
            </span>
            {syllabusExpanded ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
          </button>
          {syllabusExpanded && (
            <div className="p-4 text-xs sm:text-sm text-slate-300 leading-relaxed border-t border-[#2b2d39] bg-[#16171f]">
              <MathText text={note.syllabus_mapping} />
            </div>
          )}
        </div>
      )}

      {/* Quick Jump Anchors (Table of Contents) */}
      {headings.length > 2 && (
        <div className="mb-8 p-4 bg-[#1a1b23] border border-[#2a2c38] rounded-xl">
          <div className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2.5">
            Quick Navigation:
          </div>
          <div className="flex flex-wrap gap-2">
            {headings.filter(h => h.level <= 2).map((h, i) => (
              <a
                key={i}
                href={`#${h.id}`}
                className="text-xs px-2.5 py-1 rounded-md bg-[#242633] text-slate-300 hover:text-white hover:bg-sky-500/20 hover:border-sky-500/40 border border-transparent transition-all truncate max-w-xs"
              >
                <MathText text={h.text} />
              </a>
            ))}
          </div>
        </div>
      )}

      {/* Body Content */}
      <main className="prose prose-invert max-w-none">
        <ContentRenderer 
          content={note.content} 
          onOpenImage={onOpenImage}
          fontSizeMultiplier={fontSizeMultiplier}
        />
      </main>

      {/* Bottom Prev / Next Nav */}
      <footer className="mt-16 pt-6 border-t border-[#2d2f3c] flex flex-col sm:flex-row items-center justify-between gap-4">
        {prevTopic ? (
          <button
            onClick={() => onSelectTopic(prevTopic.topic_id)}
            className="w-full sm:w-auto text-left p-3.5 rounded-xl bg-[#1a1b23] border border-[#2b2d39] hover:border-sky-500/40 hover:bg-[#222430] transition-all group flex items-center gap-3"
          >
            <ArrowLeft size={16} className="text-slate-400 group-hover:text-sky-400 transition-colors shrink-0" />
            <div className="min-w-0">
              <div className="text-[10px] uppercase font-bold text-slate-500 tracking-wider">Previous Topic</div>
              <div className="text-xs font-semibold text-white truncate max-w-xs">{prevTopic.topic_title}</div>
            </div>
          </button>
        ) : <div />}

        {nextTopic && (
          <button
            onClick={() => onSelectTopic(nextTopic.topic_id)}
            className="w-full sm:w-auto text-right p-3.5 rounded-xl bg-[#1a1b23] border border-[#2b2d39] hover:border-sky-500/40 hover:bg-[#222430] transition-all group flex items-center justify-end gap-3"
          >
            <div className="min-w-0">
              <div className="text-[10px] uppercase font-bold text-slate-500 tracking-wider">Next Topic</div>
              <div className="text-xs font-semibold text-white truncate max-w-xs">{nextTopic.topic_title}</div>
            </div>
            <ArrowRight size={16} className="text-slate-400 group-hover:text-sky-400 transition-colors shrink-0" />
          </button>
        )}
      </footer>
    </article>
  );
}
